# servicioEntrega_Paquetes
Los servicios de entrega de paquetes como lo son Servientrega®, Envia y Coordinadora,
ofrecen una serie de diferentes opciones de envío, cada uno con un costo especifico asociado.
Crear una jerarquía de herencia para presentar diferentes tipos de paquetes. 
Use la clase “Package” como clase base de la jerarquía, incluya dos clases
“StandardPackage” y “OverweightPackage”, que hereden de la clase base “Package”.

La clase base “Package” debería incluir datos como código, peso (Kg) y costo por gramos y 
descripción del paquete. El constructor de la clase “Package” debe inicializar estos 
miembros de datos. Asegúrese de que el peso y el costo por gramos contienen valores 
positivos. La clase “Package” debe proporcionar un método público “calculate” que
devuelve un valor real que indica el costo asociado al envió del paquete, el método 
determina el costo del paquete, se multiplica el peso por el costo por gramos.

La clase derivada “StandardPackage” deberá heredar las funcionalidades de la clase base
“Package”, pero también debe incluir un miembro de datos que represente una cuota fija 
de los cargos de envió para el servicio de dos días de entrega, el constructor de esta clase 
debe tener un valor inicial que inicialice los miembros de la clase. “StandardPackage” 
debe redefinir el método “calculate” que calcule el costo de envió mediante la adición de 
la cuota fija al costo basado en el peso del paquete.

La clase “OverweightPackage” debe heredar directamente de la clase “Package” y 
contener miembro de datos adicionales que representen el costo por el sobre peso. 
“OverweightPackage” debe redefinir la función “calculate”, para que añada el cargo 
adicional por gramos antes de calcular el costo del envío.
