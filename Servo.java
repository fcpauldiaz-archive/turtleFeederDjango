/*
 * Universidad del Valle de Guatemala
 * Pablo Diaz 13203
 * William Orozco 13386
 * Adolfo Morales 13014
 * Javier Merida
 */

import com.pi4j.wiringpi.SoftPwm;

public class Servo {
    
    public static void main(String[] args) throws InterruptedException {
        
        // initialize wiringPi library
        com.pi4j.wiringpi.Gpio.wiringPiSetup();

        // create soft-pwm pins (min=0 ; max=100)
        //crear pines con pulse width modulation (id pin , min, max)
        SoftPwm.softPwmCreate(0, 0, 100);

        // continuous loop
        int contador = 0;
        while (true) {            
            // girar a la derecha
            for (int i = 0; i <= 29; i++) {
                SoftPwm.softPwmWrite(0, i);
                Thread.sleep(20);
            }
            // girar a la izquierda
            for (int i = 29; i >= 0; i--) {
                SoftPwm.softPwmWrite(0, i);
                Thread.sleep(20);
            }
            contador++;
            System.out.println(contador);
            if (contador==Integer.parseInt(args[0]))
                break;
        }
    }
}
