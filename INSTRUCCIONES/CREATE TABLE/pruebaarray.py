f = open("reportes/tc.html", "w")
f.write("<!DOCTYPE html>")
f.write("<html lang=\"en\" class=\"no-js\">")
f.write("")
f.write("<head>")
f.write("    <meta charset=\"UTF-8\" />")
f.write("    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge,chrome=1\">")
f.write("    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">")
f.write("    <title>Type Checker </title>")
f.write("    <meta name=\"description\"")
f.write("        content=\"Sticky Table Headers Revisited: Creating functional and flexible sticky table headers\" />")
f.write("    <meta name=\"keywords\" content=\"Sticky Table Headers Revisited\" />")
f.write("    <meta name=\"author\" content=\"Codrops\" />")
f.write("    <link rel=\"shortcut icon\" href=\"../favicon.ico\">")
f.write("    <link rel=\"stylesheet\" type=\"text/css\" href=\"css/normalize.css\" />")
f.write("    <link rel=\"stylesheet\" type=\"text/css\" href=\"css/demo.css\" />")
f.write("    <link rel=\"stylesheet\" type=\"text/css\" href=\"css/component.css\" />")
f.write("</head>")

f.write("<body>")
f.write("    <div class=\"container\">")
f.write("        <!-- Top Navigation -->")
f.write("        <header>")
f.write("            <h1>Type Checker</h1>")
f.write("        </header>")
f.write("        <div class=\"component\">")
f.write("            <table>")
f.write("                <thead>")
f.write("                    <tr>")
f.write("                        <th>No.</th>")
f.write("                        <th>TABLA</th>")
f.write("                        <th>ID</th>")
f.write("                        <th>TIPO</th>")
f.write("                        <th>RESTRICCION</th>")
f.write("                        <th>REFERENCIA</th>")
f.write("                        <th>TABLA REFERENCIA</th>")
f.write("                    </tr>")
f.write("                </thead>")
f.write("                <tbody>")
f.write("                    <tr>")
f.write("                        <td class=\"text-left\">x</td>")
f.write("                        <td class=\"text-left\">int</td>")
f.write("                        <td class=\"text-left\">Parametro</td>")
f.write("                        <td class=\"text-left\">Sentencias_Basicas</td>")
f.write("                        <td class=\"text-left\">0</td>")
f.write("                        <td class=\"text-left\">0</td>")
f.write("                        <td class=\"text-left\">0</td>")
f.write("                    </tr>")
f.write("                </tbody>")
f.write("            </table>")
f.write("        </div>")
f.write("    </div><!-- /container -->")
f.write("    <script src=\"http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js\"></script>")
f.write("    <script src=\"http://cdnjs.cloudflare.com/ajax/libs/jquery-throttle-debounce/1.1/jquery.ba-throttle-debounce.min.js\"></script>")
f.write("    <script src=\"js/jquery.stickyheader.js\"></script>")
f.write("</body>")
f.write("")
f.write("</html>")
f.close()