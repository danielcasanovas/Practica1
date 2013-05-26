teacherAvaluation
=================

Pràctica 2 – Desenvolupament de una aplicació web bàsica , Sistemes i tecnologies web , GEI 2012/2013 , EPS , Universitat de Lleida – Daniel Casanovas Gayoso i Diego Gaspar Casamayor

Github públic : git@github.com:danielcasanovas/Practica1.git

En aquesta part de la pràctica , hem desenvolupat els mètodes per tal de la interacció entre usuari- Web, tal com demanava a l’enunciat per tal de poder Crear, eliminar y modificar instàncies de la nostra aplicació així com fer els autocomplete proposats.

(2,5 puntos) Permitir que los usuarios registrados creen nuevas instancias de los objetos del modelo, siempre que tenga sentido que los usuarios las creen.

En la nostra aplicació hem permès a l’usuari crear qualsevol tipus de instància associada a la base de dades, sempre i quan estigui loguejat.
Així doncs, si vols crear una Avaluació de Professor assignatura, pot ser que sigui impartida nova aquest any, per tant hauràs de crear segurament una nova assignatura, un nou professor , i per suposat una nova Avaluació que estarà composta pels anteriors paràmetres.


(2,5 puntos) Permitir que los usuarios modifiquen instancias de objetos, por ejemplo que puedan modificar las instancias creadas por ellos mismos.

A part de poder crear instancies a la nostra aplicació, pots modificar també qualsevol instancia creada anteriorment, sempre i quan estiguis loguejat. Així pots rectificar qualsevol cosa creada anteriorment, o bé alguna avaluació mal feta.




(1 punto) Permitir que los usuarios borren instancias de los objetos del modelo, normalmente las creadas por ellos mismos.

Qualsevol usuari pot eliminar un professor, una assignatura, una carrera o una avaluació, així doncs pot ser que aquell professor ja no imparteixi classes, o deixi de existir alguna assignatura, i per tant l’avaluació queda obsoleta.

(1,5 puntos) Obtener las opciones de autocompletado a partir de una estructura JSON estática definida localmente. Por ejemplo, en el propio template que contiene el formulario y el código Javascript, aunque se valorará que se carguen los datos de un fichero independiente.

En aquest tipus d’autocomplete, el parametre que hem utilitzat per poder fer-lo anar és al nom de professor. Hem agafat una llista de noms comuns, els quals estan a l’arxiu “name.json”, de la carpeta “static” d’allí els agafa la nostra funció d’autocompletat de noms propis.


(1,5 puntos) Obtener las opciones de autocompletado de manera remota, desde un servicio web remoto que, a las consultas con lo que ha escrito hasta el momento el usuario en la entrada del formulario, responde con posible opciones de autocompletado, por ejemplo mediante JSON.

En aquest cas d’autocomplete, hem utilitzat la web/repositori : http://www.geonames.org/export/codes.html

Així doncs, passant-li el paràmetre “A” a la funció que agafa els noms, podem obtenir tots els països, per després obtenir-los al autocomplete. Aquesta funció la fem servir a la creació i modificació de país d’origen del professor. 

Altres consideracions:

Qualsevol usuari creat, pot modificar la seva contrasenya, sempre i quan siguin iguals(Script per comprovar que ens passen els mateixos passwords).

Només els usuaris loguejats poden utilitzar la web com a WEB 2.0.

=================

Pràctica 1 – Desenvolupament de una aplicació web bàsica , Sistemes i tecnologies web , GEI 2012/2013 , EPS , Universitat de Lleida – Daniel Casanovas Gayoso i Diego Gaspar Casamayor

Github públic : git@github.com:danielcasanovas/Practica1.git

En aquesta practica tal i com sens demanava , hem desenvolupat una aplicació web bàsica que tingues accés a les dades de una base de dades , utilitzant les eines proporcionades per Django.

L’aplicació llista el contingut de les entitats pròpies de una base de dades creada per nosaltres : Carrera <-> Assignatura <-> Professor <-> Evaluacio

A mes de llistar totes les instancies de una classe de forma general , l’aplicació permet mostrar les dades especifiques de cada instancia ja sigui una Carrera , Assignatura o un Professor.


Per accedir a l'informació a tavés de la direcció url que tenim definida és el següent:

/teachers/ - Visualitzar tots els professors de la nostra BD.
/teachers/{ID teacher}* - Visualitzar un professor en concret i els seus atributs.

/degrees/ - Visualitzar totes les carreres de la nostra DB.
/degrees/{ID degree}* - Visualitzar una  carrera en concret i els seus atributs.

/subjects/ - Visualitzar totes les assignatures de la nostra DB.
/subjects/{ID subject}* - Visualitzar una  assignatura en concret i els seus atributs.

/evaluations/ - Visualitzar totes les evaluacions segons assignatura i professor de la nostra DB.

Cal tenir en compte, que des de visualitzar una assignatura (/subjects/{ID degree}*) ens mostarà el professor, que imparteix aquella assignatura, accedint al fer clic directament a (/teachers/{ID teacher}*) del professor corresponent.

/login/ - Permet fer login d'usuari, i mostra a partir del login “correcte” el nom d'usuari a totes les demés pestanyes de l'aplicació web.

/logout/ - Tanca la sessió del usuari ja loguejat mostrant un missatge reutilitzant la pàgina mainpage.html utilitzant el “contentbody”.

/admin/  - Permet entrar com a administrador i fer operacions amb la nostra BD ( visualitzar dades, inserir dades, borrar-les)

Serà el mateix per les demés associacions on qualsevol d'elles contingui uns atributs que poden ser visualitzats amb més detall.

*Fiquem un Integer, que correspondrà a cada ID segons el model en concret que volguem veure.




