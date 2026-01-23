from flask import Flask,render_template,redirect,request,url_for,send_file
import hashlib,io
import mysql.connector as SQLC


app = Flask(__name__)


# database config
def databaseConnection():
    return SQLC.connect(
        host = 'localhost',
        user = 'root',
        password ='mysql123',
        database='filedb'

    )


# table creation function
def create_table():
    table_create_query = """CREATE TABLE IF NOT EXISTS FILES(
    FILEID INT AUTO_INCREMENT PRIMARY KEY,
    FILENAME VARCHAR(100) NOT NULL,
    FILEDATA LONGBLOB NOT NULL,
    MIMETYPE VARCHAR(20) NOT NULL,
    FILESIZE FLOAT,
    FILEHASH VARCHAR(80),
    CREATED_AT DATETIME DEFAULT CURRENT_TIMESTAMP
    );"""
    # db_config function calling
    db_config = databaseConnection()
    cursor = db_config.cursor()
    cursor.execute(table_create_query)
    cursor.close()
    db_config.close()
    return True


# home route for 
@app.route('/')
def upload_file():

    return render_template('upload.html')

@app.route('/upload',methods=['POST'])
def upload():
    file = request.files.get('file')


    if not file or file.filename == "":
        return "No File Selected"
    

    file_data = file.read()
    file_hash = hashlib.sha256(file_data).hexdigest()


    #db connection
    db_config = databaseConnection()
    cursor = db_config.cursor()
    mimetype = file.mimetype
    #file duolicate check

    cursor.execute(
        "select * from files where filename = %s and filehash = %s;",(file.filename,file_hash)
    )


    if cursor.fetchone():
        cursor.close()
        db_config.close()
        return render_template('upload.html',msg = "File Already Exists")


    #insert file metadata into table
    cursor.execute(
        "insert into files(filename,filedata,mimetype,filehash,filesize) values(%s,%s,%s,%s,%s)",
        (file.filename,file_data,mimetype   ,file_hash,len(file_data)) #file.mimetype = mimetype
    )

    db_config.commit()
    cursor.close()
    db_config.close()
    # get file meta data

    if file:
        return "File Uploaded Successfully"
    return "file note uploaded"






@app.route('/files',methods=['POST','GET'])
def view_files():
    
    # get files from db
    get_files_query = "select fileid,filename,filedata,mimetype from files "
    db_config = databaseConnection()
    cursor = db_config.cursor(dictionary = True)
    cursor.execute(get_files_query)
    files = cursor.fetchall()
    cursor.close()
    db_config.close()
    return render_template('files.html',files = files)



# get file from database ising fileid
def get_file(file_id):
    db_config = databaseConnection()
    cursor = db_config.cursor()
    get_file_query = """SELECT FILEID ,FILENAME,FILEDATA,MIMETYPE FROM FILES WHERE FILEID = %s;"""
    cursor.execute(get_file_query, (file_id,))
    file = cursor.fetchone()
    cursor.close()
    db_config.close()
    return file

# view file browser
@app.route('/view/<int:file_id>')
def file_view(file_id):
    file = get_file(file_id=file_id)
    fileid,filename,filedata,mimetype = file


    # view file in browser
    return send_file(io.BytesIO(filedata),
              mimetype = mimetype,
              download_name = filename,
              as_attachment = False )


# # download  file browser
@app.route('/download/<int:file_id>')
def file_download(file_id):
    file = get_file(file_id=file_id)
    fileid,filename,filedata,mimetype = file


    # view file in browser
    return send_file(io.BytesIO(filedata),
              mimetype = mimetype,
              download_name = filename,
              as_attachment = True )

# delete file from browser 
@app.route('/delete/<int:file_id>')
def file_delete(file_id):
    db_config = databaseConnection()
    cursor = db_config.cursor()
    cursor.execute("delete from files where fileid = %s;",(file_id,))
    db_config.commit()
    cursor.close()
    db_config.close()
    return redirect(url_for('view_files'))

# main 
if __name__ == '__main__':
    create_table()
    app.run(debug=True)

