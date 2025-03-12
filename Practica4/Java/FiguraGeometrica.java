package polimorfismo;

public class FiguraGeometrica {
	
	
	double area(double radio) {
		return Math.PI * radio * radio; //Circulo
	}
	
	double area(double base, double altura) {
		return base * altura; //Rectangulo
	}
	
	double area(double base, float altura) {
		return (base * altura) / 2; //Triangulo Rectangulo 
	}
	
	double area(double baseMenor, double baseMayor, double altura) {
		return ((baseMenor + baseMayor) * altura) / 2; //Trapecio
	}
	
	double area(float perimetro, float apotema) {
		return (perimetro * apotema) / 2; //Pentagono
	}
	
	public static void main(String[] args) {
		FiguraGeometrica f1 = new FiguraGeometrica();
		FiguraGeometrica f2 = new FiguraGeometrica();
		FiguraGeometrica f3 = new FiguraGeometrica();
		FiguraGeometrica f4 = new FiguraGeometrica();
		FiguraGeometrica f5 = new FiguraGeometrica();
		System.out.println("Circulo: " + f1.area(1));
	    System.out.println("Rectángulo: " + f2.area(3, 4));
	    System.out.println("Triángulo Rectángulo: " + f3.area(5, 6));
	    System.out.println("Trapecio: " + f4.area(3, 5, 4));
	    System.out.println("Pentágono: " + f5.area(10, 7));
	}

}
