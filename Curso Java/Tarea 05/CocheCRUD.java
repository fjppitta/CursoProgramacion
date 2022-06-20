package com.tareas;
import com.tareas.Coche;
import java.util.ArrayList;
import java.util.List;

public interface CocheCRUD {

    void save(Coche coche);
    void delete(Coche coche);
    List<Coche> findAll();

}
