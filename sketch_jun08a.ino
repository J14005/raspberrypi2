int val = 0; //入力される値を格納する為の変数
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}
 
void loop() {
  // put your main code here, to run repeatedly:
  //ANALOG INの０番ピンからデータを受け取る
  val=analogRead(0);
  Serial.println(val);
  delay(500);
}

