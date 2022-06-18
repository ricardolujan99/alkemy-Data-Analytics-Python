CREATE TABLE tabla_completa (
    Cod_localidad text,
    Id_provincia text,
    Id_departamento text,
    Categoria text,
    Provincia text,
    Localidad text,
    Nombre text,
    Domicilio text,
    Codigo_postal text,
    Número_de_teléfono text,
    Mail text,
    Web text
    );

CREATE TABLE datos_salas_de_cine (
    Provincia text,
    Pantallas text,
    Butacas text,
    espacio_INCAA text
);

 
CREATE TABLE registros_totoales(
    total_por_categoria text,
    totoal_por_fuente text,
    provincia_y_categoria text
);