teacherAvaluation
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




