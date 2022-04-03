Algoritmo decimal_a_fraccion_irreductible
	// He definido decimal como caracter o string de carac a implementar las validacion de que este comprendido entre 0 y 0.9999 y no permita caracteres  distintos de los numericos
	Definir decimal Como Caracter;
	Escribir 'Introduce un número entre 0 y 0.9999 con un maximo de 4 digitos decimales: ';
	Leer decimal;
	// estas variables a continuacion son solo para validar el input
	Definir tamanno_decimal,numerador,i Como Entero;
	Definir control_solo_numeros_en_decimal,control_un_solo_punto Como Logico;
	tamanno_decimal <- Longitud(decimal);
	control_solo_numeros_en_decimal <- Verdadero;
	control_un_solo_punto <- Verdadero;
	// Esto es un artificio para validar que metemos un numero entre 0 y 0.9999 debido a la naturaleza de PSeint por los tipos que contiene parece mas complejo de lo que en realidad es
	// SImplemente recorro el tamaño de la cadena introducida y compruebo que todos sus caracteres sean o 1-9 o un solo punto "."
	// tampoco me permite poner la condición de los Si en varias lineas
	// en otro de lenguaje esta validacion seria mucho mas sencilla.
	Para i<-0 Hasta tamanno_decimal-1 Hacer // El -1 que resto a tamaño inicial es porque Pseint guarda el caracter de retroceso en la cadena
		Si Subcadena(decimal,i,i)=='.' Y i<>1 Entonces
			control_un_solo_punto <- Falso;
		FinSi
		Si Subcadena(decimal,i,i)<>'0' Y Subcadena(decimal,i,i)<>'1' Y Subcadena(decimal,i,i)<>'2' Y Subcadena(decimal,i,i)<>'3' Y Subcadena(decimal,i,i)<>'4' Y Subcadena(decimal,i,i)<>'5' Y Subcadena(decimal,i,i)<>'6' Y Subcadena(decimal,i,i)<>'7' Y Subcadena(decimal,i,i)<>'8' Y Subcadena(decimal,i,i)<>'9' Y Subcadena(decimal,i,i)<>'.' Entonces
			control_solo_numeros_en_decimal <- Falso;
		FinSi
	FinPara
	Mientras Subcadena(decimal,0,1)<>'0.' O tamanno_decimal>6 O control_solo_numeros_en_decimal=Falso O control_un_solo_punto=Falso Hacer
		Escribir 'Error: Debes introducir un numero entre 0 y 0.9999 y con solo 4 dígitos decimales';
		Leer decimal;
		tamanno_decimal <- Longitud(decimal);
		control_solo_numeros_en_decimal <- Verdadero;
		control_un_solo_punto <- Verdadero;
		Para i<-1 Hasta tamanno_decimal-1 Hacer // El -1 que resto a tamaño inicial es porque Pseint guarda el caracter de retroceso en la cadena
			Si Subcadena(decimal,i,i)=='.' Y i<>1 Entonces
				control_un_solo_punto <- Falso;
			FinSi
			Si Subcadena(decimal,i,i)<>'0' Y Subcadena(decimal,i,i)<>'1' Y Subcadena(decimal,i,i)<>'2' Y Subcadena(decimal,i,i)<>'3' Y Subcadena(decimal,i,i)<>'4' Y Subcadena(decimal,i,i)<>'5' Y Subcadena(decimal,i,i)<>'6' Y Subcadena(decimal,i,i)<>'7' Y Subcadena(decimal,i,i)<>'8' Y Subcadena(decimal,i,i)<>'9' Y Subcadena(decimal,i,i)<>'.' Entonces
				control_solo_numeros_en_decimal <- Falso;
			FinSi
		FinPara
	FinMientras
	// Este es el algoritmo de reducir a fraccion irreducible propiamente , he optado por buscar el maximo comun divisor de ambos
	numerador <- ConvertirANumero(decimal)*10000;
	Escribir numerador;
	denominador <- 10000;
	i <- numerador;
	Repetir
		Si numerador MOD i==0 Y denominador MOD i==0 Entonces
			numerador <- numerador/i;
			denominador <- denominador/i;
		FinSi
		i <- i-1;
	Mientras Que i>1
	Escribir numerador,'/',denominador;
FinAlgoritmo
