print "Context-Type: text/html"
print ""

import cgi, cgitb
form=cgi.FieldStorage()
val=form.getvalue('file')

print """
<head>

	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">

	<title>Update Incident</title>

	<link rel="stylesheet" href="update.css">

<body>



    <div class="main-content">

        <!-- You only need this form and the form-basic.css -->

        <form class="form-basic" method="post" action="cgi-bin/create.py" style="margin-top:6%; margin-bottom:6%;">

            <div class="form-title-row">
                <h1>Update Incident</h1>
            </div>



            <div class="form-row">
                <label>
                    <span>Status:</span>
                    <select name="status" style="width:100px;">
                        <option value="red">RED</option>
                        <option value="amber">AMBER</option>
                        <option value="resolved">Resolved</option>

                    </select>
                </label>
            </div>



            <div class="form-row">
                <label>
                    <span>Subject:</span>
                    <textarea name="subject" style="margin-left:5%;" required="required"></textarea>
                </label>
            </div>







            <div class="form-row">
<!--                <label>
                    <span>Description</span>
                    <textarea name="desc" style="height:200px; margin-left:3%;"></textarea>
                </label>

-->
<label>
                    <span>Description:</span>
                </label>

<iframe class="form-row" src=%s style="
    width: 90%;
    height: 600px;
    margin-left: 5%;
">
</iframe>
            </div>
"""%(val)


print """
            <div class="form-row">

<button style="margin-left:50%"><a href="abc.html" >Create</a></button>
       <!--         <button type="submit" onclick="myFunction()";>Save</button>
-->
        </div>

        </form>
<!--   <script>
	function myFunction() {
	alert("Outage Send..");}
   </script>
	
-->
    </div>

</body>
"""

