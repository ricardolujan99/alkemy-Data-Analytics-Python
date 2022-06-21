CREATE TABLE tabla_completa (
    Cod_localidad text,
    Id_provincia text,
    Id_departamento text,
    Categoria text,
    Provincia text,
    Localidad text,
    Nombre text,
    Domicilio text,
    "Codigo postal" text,
    "Número de teléfono" integer,
    Mail text,
    Web text,
    "Fecha y hora registro" timestamp      
    );

CREATE TABLE datos_salas_de_cine (
    Provincia text,
    Pantallas integer,
    Butacas integer,
    espacio_INCAA integer,
    "Fecha y hora registro" timestamp      
);

 
CREATE TABLE registros_totoales(
    "Index" text,
    "Total por categoria" integer,
    "Totoal por fuente" integer,
    "Provincia y categoria" integer,
    "Fecha y hora registro" timestamp      

);