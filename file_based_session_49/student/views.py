from django.shortcuts import render

'''
setting.py-> write now
#File based session
SESSION_ENGINE = 'django.contrib.sessions.backends.file'
SESSION_FILE_PATH = BASE_DIR/'session'
'''

# Set file views here.
def set_file_session(request):
    request.session['name'] = 'sadiya'
    return render(request, 'student/setfile.html')

# Set file views here.
def get_file_session(request):
    name = request.session['name']
    return render(request, 'student/getfile.html', {'name':name})

# Delete file views here.
def del_file_session(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'student/delfile.html')
