import cherrypy
import os
from datetime import datetime

class HelloWord(object):
    @cherrypy.expose()
    def index(self):
        return 'Hello World'

    @cherrypy.expose()
    def get_date(self):
        return str(datetime.now())

    @cherrypy.expose()
    def greetings(self, name='Sanku', last=None):
        cherrypy.session['my_string'] = '%s %s' %(name, last)
        return 'Hello ' + name

    @cherrypy.expose()
    def display(self):
        return 'You had entered: ' + cherrypy.session['my_string']

    @cherrypy.expose()
    def input_form(self):
        return '''
        <HTML>
            <TITLE>FORM</TITLE>
            <HEAD>
                <LINK href='/static/css/style.css' rel='stylesheet' ></LINK>
            </HEAD>
            <BODY>
                <FORM METHOD="GET" ACTION="greetings">
                    <INPUT TYPE="TEXT" NAME="name" VALUE="David" ></INPUT>
                    <INPUT TYPE="TEXT" NAME="last" VALUE="Song" ></INPUT>
                    <BUTTON TYPE="SUBMIT">SUBMIT</BUTTON>
                </FORM>
            
            </BODY>
        
        </HTML>
        
        
        '''




if __name__ == '__main__':
    conf = {
        '/': {'tools.sessions.on' : True,
              'tools.staticdir.root': os.path.abspath(os.getcwd())},

        '/static': {'tools.staticdir.on': True,
                    'tools.staticdir.dir': './public'}

    }
    cherrypy.quickstart(HelloWord(), '/', conf)
