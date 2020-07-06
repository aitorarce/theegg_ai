Algoritmo pikachu
	turno = 1;
	pikachu_vida = 100;
	pikachu_ataque = 55;
	jigglypuff_vida = 100;
	jigglypuff_ataque = 45;
	Mientras SI jigglypuff_vida > 0 Y pikachu_vida > 0 Hacer
		Si Si turno = 1 Entonces
			jigglypuff_vida = jigglypuff_vida-pikachu_ataque;
			turno = 0;
		SiNo
			pikachu_vida = pikachu_vida-jigglypuff_ataque;
			turno = 1;
		FinSi
	FinMientras
	Si Si pikachu_vida <=0 Entonces
		Escribir "Jigglypuff ha ganado";
	SiNo
		Escribir "pikachu ha ganado";
	FinSi
FinAlgoritmo
