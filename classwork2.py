from sqlachemy import select
with engine.connect() as connection:
    statement=select(students)
    result=connection.execute(statement)
    for rom in result:
        print(row.id,row.name,row.is_active)
    statement2=select(students.c.name,students.c.gpa)
    result2=connection.execute(statement2)
    for row in result2:
        print(row.name,row.gpa)
from sqlachemy import update,delete
with engine.connect() as connection:
    statement=(update(students_table).where(students_table.c.name=='Petrov P.P.')
               .values(gpa=4.6))
    result=connection.execute(statement)
    connection.commit()
    print(f"обновление строк: {result.rowcount}")
    statement2=(delete(students_table).where(students_table.c.gpa<3.5))
    result=connection.execute(statement2)
    connection.commit()