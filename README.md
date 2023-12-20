<h1>Blog App using Django</h1>

<p>Submitted By Kartikey Sharma</p>

<h2>Table of Contents</h2>

<ul>
<li><a href="#installation">Installation</a></li>
<li><a href="#usage">Usage</a></li>
</ul>

<h2 id="installation">Installation</h2>

<h3>Clone the Repository</h3>

<pre><code>git clone https://github.com/J0nTyy/ZedBlock-Project.git
cd ZedBlock-Project
</code></pre>

<h3>Create and Activate Virtual Environment (Optional)</h3>

<pre><code>python -m venv venv
source venv/bin/activate  <!-- On macOS/Linux -->
venv\Scripts\activate  <!-- On Windows -->
</code></pre>

<h3>Install Dependencies</h3>

<pre><code>pip install -r requirements.txt
</code></pre>

<h3>Apply Migrations</h3>

<pre><code>python manage.py migrate
</code></pre>

<h2 id="usage">Usage</h2>

<h3>Run Development Server</h3>

<pre><code>python manage.py runserver
</code></pre>

<p>Visit <a href="http://localhost:8000">http://localhost:8000</a> in your web browser.</p>


<h3>Access Admin Panel</h3>

<p>Visit <a href="http://localhost:8000/admin">http://localhost:8000/admin</a> and log in with your superuser credentials.</p>
