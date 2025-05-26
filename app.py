from flask import Flask, render_template, request, redirect, url_for, session
from utils.layer3 import generate_combined_report

app = Flask(__name__)
app.secret_key = '123'  # Required for session

def generate_embed_html(link):
    return f'''
        <a href="{link}" target="_blank">
          <img src="/static/placeholder.jpeg" alt="News Preview" style="width:100%; height:auto; object-fit:cover;" />
        </a>
    '''

@app.route('/', methods=['GET', 'POST'])
def display_report():
    if request.method == 'POST':
        user_prompt = request.form['user_prompt']
        result = generate_combined_report(user_prompt)
        session['score'] = result["score"]
        session['embed_codes'] = [generate_embed_html(link) for link in result["links"]]
        session['report'] = result["report"]
        return redirect(url_for('display_report'))

    # Use get() so values persist in session
    score = session.get('score')
    embed_codes = session.get('embed_codes', [])
    report = session.get('report', "")
    return render_template("index.html", score=score, embed_codes=embed_codes, report=report)

@app.route('/reset')
def reset():    
    session.pop('score', None)
    session.pop('embed_codes', None)
    session.pop('report', None)
    return redirect(url_for('display_report'))


if __name__ == '__main__':
    app.run(debug=True)