const int PIN_SENSOR_EMG = A0; // Pin analógico para leer el sensor EMG
const int PIN_LED = 13; // Pin digital para controlar el LED
const int TAMANO_VENTANA = 50; // Tamaño de la ventana para el cálculo de la varianza
const int UMBO_VARIANZA = 3402; // Umbral de varianza para detectar flexión/extensión determinado en python con el promedio de las 10 muestras anteriores :D
const int ORDEN_FILTRO = 4; // Orden del filtro IIR
const float FRECUENCIA_CORTE = 10.0; // Frecuencia de corte del filtro IIR pasa altas

// Coeficientes del filtro IIR pasa altas
const float COEFICIENTE_A[ORDEN_FILTRO + 1] = {1,  -3.83582554, 5.52081914, -3.53353522, 0.848556};
const float COEFICIENTE_B[ORDEN_FILTRO + 1] = {0.92117099, -3.68468397, 5.52702596, -3.68468397, 0.92117099};

int datosEMG[TAMANO_VENTANA] = {0}; // almacenar los valores EMG, inicializsdo con ceros
int indiceDatos = 0; // indice para el arreglo

void setup() {
  Serial.begin(9600); // comunicación serial
  pinMode(PIN_LED, OUTPUT); // Configurar el pin del LED como salida
  // Enciende el LED manualmente como prueba
  digitalWrite(PIN_LED, HIGH);
  delay(1000); // Espera 1 segundo
  digitalWrite(PIN_LED, LOW);
}

void loop() {
  int valorSensor = analogRead(PIN_SENSOR_EMG); // Leer el valor del sensor EMG
  int valorFiltrado = aplicarFiltroIIR(valorSensor); // Filtrar el valor EMG con un filtro IIR pasa altas
  datosEMG[indiceDatos] = valorFiltrado; // Almacenar el valor filtrado en el arreglo
  indiceDatos = (indiceDatos + 1) % TAMANO_VENTANA; // Actualizar el índice para que se desplace 

  float media = calcularMedia(datosEMG, TAMANO_VENTANA); // Calcular la media de los valores EMG filtrados
  float varianza = calcularVarianza(datosEMG, TAMANO_VENTANA, media); // Calcular la varianza

  Serial.println(varianza); // Enviar la varianza a través del puerto serial

  if (varianza > UMBO_VARIANZA) {
    digitalWrite(PIN_LED, HIGH); // Encender el LED
  } else {
    digitalWrite(PIN_LED, LOW); // Apagar el LED
  }
}

// DEFINICION DE FUNCIONES 

float calcularMedia(int* datos, int tamano) {
  long suma = 0;
  for (int i = 0; i < tamano; i++) {
    suma += datos[i];
  }
  return (float)suma / tamano;
}

float calcularVarianza(int* datos, int tamano, float media) {
  long diferenciasAlCuadrado = 0;
  for (int i = 0; i < tamano; i++) {
    float diferencia = datos[i] - media;
    diferenciasAlCuadrado += diferencia * diferencia;
  }
  return (float)diferenciasAlCuadrado / tamano;
}

int aplicarFiltroIIR(int valor) {
  static float bufferEntrada[ORDEN_FILTRO + 1] = {0}; // Arreglo para almacenar los valores de entrada anteriores
  static float bufferSalida[ORDEN_FILTRO + 1] = {0}; // Arreglo para almacenar los valores de salida anteriores

  // Desplazar los valores de entrada y salida anteriores
  for (int i = ORDEN_FILTRO; i > 0; i--) {
    bufferEntrada[i] = bufferEntrada[i - 1];
    bufferSalida[i] = bufferSalida[i - 1];
  }
  bufferEntrada[0] = valor; // Nuevo valor de entrada

  // Calcular la salida filtrada
  bufferSalida[0] = 0;
  for (int i = 0; i <= ORDEN_FILTRO; i++) {
    bufferSalida[0] += COEFICIENTE_B[i] * bufferEntrada[i];
  }
  for (int i = 1; i <= ORDEN_FILTRO; i++) {
    bufferSalida[0] -= COEFICIENTE_A[i] * bufferSalida[i];
  }

  return (int)bufferSalida[0]; // Retornar el valor filtrado
}
