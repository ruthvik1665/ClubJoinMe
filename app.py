from flask import Flask, render_template

app = Flask(__name__)

post=[{'designation':'president','des':'Need to be perfect in managing people,good leadership qualities,profound communication skills'
      },
      {'designation':'vice president',
       'img':' "https://clubjoinme.ruthvikbasetti.repl.co/cs" ','des':'Need to be perfect in managing people,good leadership qualities,profound communication skills'
      },
      {'designation':'club member','des':'Need to be perfect in managing people,good leadership qualities,profound communication skills'
      },
      {'designation':'club member',
       'des':'Need to be perfect in managing people,good leadership qualities,profound communication skills'
      },
      {'designation':'club member','des':'Need to be perfect in managing people,good leadership qualities,profound communication skills'
      }]
@app.route("/")
def hello_world():
  return render_template('home.html')

@app.route("/cs")
def cs():
  return render_template('cs.html',posts=post)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=False)
