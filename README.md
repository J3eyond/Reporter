<h1>Reporter</h1>
<h2>Description</h2>
Simple script send email with attachments.
</br>
<hr>
<h2>Install</h2>
<br>
<p><i>Clone repository:</i></p>
<pre>git clone https://github.com/J3eyond/Reporter.git</pre>

<p><i>Enter the folder:</i></p>
<pre>cd Reporter</pre>

<p><i>Install requirements:</i></p>
<pre>pip install -r requirements.txt</pre>

<p><i>Create .env file and set lines:</i></p>
<pre>
SMTP_SERVER='Smtp server'
PORT='Port number'
EMAIL='Email account'
LOGIN='Email login'
PASSWORD='Account password'
SUBJECT='Email subject'
RECEIVER='Email receiver'
MESSAGE='Text for email message'
REPORT_FOLDER='*Your_absolute_path*/Reporter/reports/'
</pre>

<h2>Attachments(optional)</h2>
<p><i><b>reports</b> - folder for your attachments.</i></p>
<p><i>If you need attachments put them in the reports folder.</i></p>


<h2>Launch</h2>
<pre>python3 reporter.py</pre>

<h2>Requirements</h2>
<hr>
<li><b>Python 3.8 +</b></li>