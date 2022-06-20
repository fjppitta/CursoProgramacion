package com.tareas;
public class Main {
    static CocheCRUD cocheCRUD = new CocheCRUDImpl() {
    };

    public static void main(String[] args) {
        Coche sedan = new Coche("Vento","VW","Verde",5);
        Coche compacto = new Coche("Pointer","VW","Blanco",3);

        cocheCRUD.save(compacto);
        cocheCRUD.save(sedan);

        System.out.println(cocheCRUD.findAll());

        cocheCRUD.delete(compacto);
        System.out.println(cocheCRUD.findAll());

      //  System.out.println(cocheCRUD.findAll());

    }
}
