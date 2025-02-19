import javax.swing.*;
import java.awt.*;

class Punto {
    public float x, y;

    public Punto(float x, float y) {
        this.x = x;
        this.y = y;
    }

    public float getX() { return x; }
    public float getY() { return y; }

    public String toString() {
        return "Punto(" + x + ", " + y + ")";
    }
}

class Linea {
    public Punto p1, p2;

    public Linea(Punto p1, Punto p2) {
        this.p1 = p1;
        this.p2 = p2;
    }

    public void dibujaLinea(Graphics g) {
        g.drawLine((int) p1.getX(), (int) p1.getY(), (int) p2.getX(), (int) p2.getY());
    }

    public String toString() {
        return "Línea entre " + p1 + " y " + p2;
    }
}

class Circulo {
    public Punto centro;
    public float radio;

    public Circulo(Punto centro, float radio) {
        this.centro = centro;
        this.radio = radio;
    }

    public void dibujaCirculo(Graphics g) {
        int x = (int) (centro.getX() - radio);
        int y = (int) (centro.getY() - radio);
        int d = (int) (2 * radio);
        g.drawOval(x, y, d, d);
    }

    public String toString() {
        return "Círculo con centro en " + centro + " y radio " + radio;
    }
}

class PanelDibujo extends JPanel {
    public Linea linea;
    public Circulo circulo;

    public PanelDibujo(Linea linea, Circulo circulo) {
        this.linea = linea;
        this.circulo = circulo;
    }

    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        linea.dibujaLinea(g);
        circulo.dibujaCirculo(g);
    }
}

public class Graficador {
    public static void main(String[] args) {
        Punto p1 = new Punto(50, 100);
        Punto p2 = new Punto(200, 200);
        Linea linea = new Linea(p1, p2);

        Punto centro = new Punto(300, 150);
        Circulo circulo = new Circulo(centro, 50);

        JFrame frame = new JFrame("Dibujando Línea y Círculo");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        frame.add(new PanelDibujo(linea, circulo));
        frame.setVisible(true);

        System.out.println(p1);
        System.out.println(p2);
        System.out.println(linea);
        System.out.println(circulo);
    }
}
