#define LEFTIN A0
#define LEFTSTOP 50
#define LEFTOUT 48


#define RIGHTIN A1
#define RIGHTOUT 44
#define RIGHTSTOP 30

void setup(){
	Serial.begin(9600);
	pinMode(LEFTIN, INPUT);
	pinMode(LEFTOUT, OUTPUT);
	pinMode(RIGHTIN, INPUT);
	pinMode(RIGHTOUT, OUTPUT);
	pinMode(A2, INPUT);
	pinMode(A3, INPUT);
}

void loop(){
	// int left = digitalRead(LEFTIN);
	// digitalWrite(LEFTOUT, left);

	// int right = digitalRead(RIGHTIN);
	// digitalWrite(RIGHTOUT, right);

	// Serial.println(String(left) + "\t" + String(right));
	int L = analogRead(LEFTIN);
	int R = analogRead(RIGHTIN);
	int pin13 = analogRead(A2);
	int pin15 = analogRead(A3);
	Serial.println(String(L) + "\t" + String(R) + "\t" + String(pin13) + "\t" + String(pin15));

	if (L > 500){
		digitalWrite(LEFTOUT, HIGH);
	}
	else{
		digitalWrite(LEFTOUT, LOW);
	}


	if (R > 500){
		digitalWrite(RIGHTOUT, HIGH);
	}
	else{
		digitalWrite(RIGHTOUT, LOW);
	}
}