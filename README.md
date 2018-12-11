<h1> <b> Reverse Shell </b> </h1>
<p> A reverse shell is a type of shell in which the target machine communicates back to the attacking machine. The attacking machine has a listener port on which it receives the connection, which by using, code or command execution is achieved.</p>
<img src="https://mk0resourcesinfm536w.kinstacdn.com/wp-content/uploads/ICMP-ReverseShell11042014.gif" align="center" />

<h2> Programme Screenshots </h2>
<img src="https://docs.google.com/uc?id=1uyv74t6MVsJYCilyR9bzUi63b3SDg8pq" width="500" height="300"/>
<img src="https://docs.google.com/uc?id=1PzhNtkaTBmFvaJWPJAB4qYC_pRnKVowS" width="500" height="300" />
<h2> Installation  </h2>
<p> Install Dependencies in requirements.txt file</p>
<ul> <li> pip install -r requirements.txt </li> </ul>
<p> While installing if error popup that saying <i> <b>Can't install cx_freeze or scipy Python 3.7 64-bit </i></b> </p>
<ul> 
  <li> Using following link Download .WHL object that compatible to your python version </li>
  <li> Link : <a href="https://www.lfd.uci.edu/~gohlke/pythonlibs/#cx_freeze" target="_blank">https://www.lfd.uci.edu/~gohlke/pythonlibs/#cx_freeze</a></li>
  <li> On your command prompt change directory to the downloaded folder and use the command: <b> pip install cx_Freeze‑5.1.1‑cp37‑cp37m‑win_amd64.whl </b></li>
  <li> re-install dependencies in requirements.txt </li>
</ul>

<h2>How to use</h2>
<ul> 
  <li> Change <b>HOST</b> variable in <b>client.py</b> to your HOST machine IP  </li>
  <li> Use setup.py to generate .exe file : <b> python setup.py build </b></li>
   <li> Run server.py and send generated .exe to victim/s </li>
  <li> Issue "list" command (server.py) to list all the connections available </li>
  <li> Issue "select [Client_Number]" command (server.py) to connect to particular client </li>
  <li> Issue "quit" command to exit from connected client </li>
</ul>

<h3> Developed By : Nisal Priyanka </h3>
<code> ** ONLY FOR THE EDUCATIONAL PURPOSE ** </code>
