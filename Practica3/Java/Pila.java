class Pila {
    private long[] arreglo;
    private int top;
    private int n;

    public Pila(int n) {
        this.n = n;
        this.arreglo = new long[n];
        this.top = -1;
    }

    public void push(long e) {
        if (isFull()) {
            System.out.println("La pila está llena");
        }
        arreglo[++top] = e;
    }

    public long pop() {
        if (isEmpty()) {
        	System.out.println("La pila está vacía");
        }
        return arreglo[top--];
    }

    public long peek() {
        if (isEmpty()) {
        	System.out.println("La pila está vacía");
        }
        return arreglo[top];
    }

    public boolean isEmpty() {
        return top == -1;
    }

    public boolean isFull() {
        return top == n - 1;
    }

    public static void main(String[] args) {
        Pila pila = new Pila(5);
        pila.push(10);
        pila.push(20);
        System.out.println(pila.pop());  
        System.out.println(pila.peek()); 
    }
}
