# Memoria Practica 1: Módul Client-Servidor
## Client
### Obrir un fitxer
En el moment accedir a un fitxer, he trobat que hi ha ues maneres diferents, una de les quals és obrint el fitxer amb file= open('nom_fitxer','mode_d_us')
utilitzant aquestes instruccions, després de tractar el fitxer, l'hem de cancar amb una altra línia de codi.
Per altra banda, hi ha una segona manera, la qual és utilitzant la funció de with ('nom_del_fitxer') as nom_alias:
amb aquesta ordre, el fitxer un cop acabat el tractament, es tanca automàticament.

## Servidor
### Ip del ordenador 
Hi ha dues maneres de trobar la teva pròpia ip per comprovar si el servidor respon correctament al client, la primera per mitjà de la terminal amb la 
sentencia de ip config, en l'apartat de "Ipv4" i declarant la variable ip manualment. 
La segona manera es cridant anfuncions que busquen directament la teva ip local, la qual és: Server = socket.gethostbyname(socket.gethostname())
No obstant aquesta opció només serveix per al moment de la reproducció del subsistema de comunicació de prova. 

### Port escollit
S'ha de tenir en compte que per no modificar ports ja utilitzats per defecte en la configuració base, utilitzem part el més allunyats possibles als primers 4000.
Els ports amb més probabilitata d'estar buits son a partir del 5000.

