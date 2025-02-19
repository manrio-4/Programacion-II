
public class Punto {
	public float x;
	public float y;
	
	public Punto(float x, float y) {
		this.x = x;
		this.y = y;
	}
	public String coord_cartesianas() {
		return "(" + x + ", " + y +")";
	}
	public String coord_polares() {
		double r = Math.sqrt(x * x + y * y);
        double theta = Math.toDegrees(Math.atan2(y, x));
        return String.format("Coordenadas Polares: (r=%.2f, θ=%.2f°)", r, theta);
	}
	public String toString() {
		return "Punto(" + x + ", " + y + ")";
	}
	public static void main(String[] args) {
		Punto p = new Punto(3.0f, 4.0f);
        System.out.println(p);
        System.out.println(p.coord_cartesianas());
        System.out.println(p.coord_polares());
	}

}
