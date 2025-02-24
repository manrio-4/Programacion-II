import javax.swing.*;
import java.awt.*;

class Punto {
    int x, y;

    public Punto(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class Linea extends JPanel {
    Punto p1, p2;

    public Linea(Punto p1, Punto p2) {
        this.p1 = p1;
        this.p2 = p2;
        setPreferredSize(new Dimension(400, 400)); 
    }

    @Override
    public void paintComponent(Graphics g) {
        g.drawLine(p1.x*20, p1.y*20, p2.x*20, p2.y*20);
    }


    public void dibujaLinea() {
        JFrame frame = new JFrame("Dibujar Línea");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(this); // Agrega el panel Linea directamente
        frame.pack(); // Ajusta el tamaño según el panel
        frame.setVisible(true);
    }
}


class Circulo extends JPanel {
    Punto centro;
    int radio;

    public Circulo(Punto centro, int radio) {
        this.centro = centro;
        this.radio = radio;
        setPreferredSize(new Dimension(400, 400)); // Tamaño del panel
    }

    public void paintComponent(Graphics g) {

        g.drawOval(centro.x*10, centro.y*10, 2 * radio * 10, 2 * radio * 10);
    }

    public void dibujaCirculo() {
        JFrame frame = new JFrame("Dibujar Círculo");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(this);
        frame.pack();
        frame.setVisible(true);
    }
}


public class Graficador {
    public static void main(String[] args) {
        Punto centro = new Punto(2, 2);
        int radio = 5;
        Circulo circulo = new Circulo(centro, radio);
        circulo.dibujaCirculo();
        Punto p1 = new Punto(5, 5);
        Punto p2 = new Punto(3, 3);
        Linea linea = new Linea(p1, p2);
        linea.dibujaLinea();
    }
}
