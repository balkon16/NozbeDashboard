# TODO: needs rework

from typing import List

from .base_saver import DataSaver
from ..entities.project import Project
# from entities.task import Task # For type hinting if processing tasks directly

# Example (if using SQLAlchemy, not fully implemented here)
# from sqlalchemy import create_engine, Column, String, DateTime, Boolean, ForeignKey, Decimal as SqlDecimal
# from sqlalchemy.orm import sessionmaker, relationship, declarative_base
# Base = declarative_base()

# class ProjectModel(Base):
#     __tablename__ = 'projects'
#     # Define columns matching Project dataclass
#     id = Column(String, primary_key=True)
#     name = Column(String)
#     created_at = Column(DateTime)
#     last_updated_at = Column(DateTime)
#     is_completed = Column(Boolean)
#     tasks = relationship("TaskModel", back_populates="project")

# class TaskModel(Base):
#     __tablename__ = 'tasks'
#     # Define columns matching Task dataclass
#     id = Column(String, primary_key=True)
#     name = Column(String)
#     duration = Column(SqlDecimal) # Use SQLAlchemy's Decimal
#     is_completed = Column(Boolean)
#     last_updated_at = Column(DateTime)
#     project_id = Column(String, ForeignKey('projects.id'))
#     project = relationship("ProjectModel", back_populates="tasks")


class SqlSaver(DataSaver):
    """
    Saves data to a relational database.
    (This is a conceptual outline and needs a full ORM or DB-API implementation)
    """

    def __init__(self, db_connection_string: str):
        self.db_connection_string = db_connection_string
        # self.engine = create_engine(db_connection_string)
        # Base.metadata.create_all(self.engine) # Create tables if they don't exist
        # self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        print(f"SQL Saver initialized for: {db_connection_string}. (Full implementation pending)")

    def _prepare_data_for_saving(self, projects: List[Project]):
        # This method from the base class flattens data, which is generally
        # not what you want for relational SQL saving where you preserve entities.
        # It's overridden here to indicate it's not used in the same way.
        raise NotImplementedError(
            "_prepare_data_for_saving is not directly applicable for relational SQL saving "
            "in its current form. SQL saving requires handling entities and relationships directly."
        )

    def save(self, projects: List[Project], filepath: str = None, **kwargs) -> None:
        """
        Saves project and task data to a relational database.
        The 'filepath' argument is ignored for DB savers but kept for interface consistency.

        Args:
            projects: A list of Project objects.
            filepath: (Ignored)
            **kwargs: Additional arguments for DB operations (e.g., batch_size).
        """
        print(f"Attempting to save {len(projects)} projects to database: {self.db_connection_string}")
        if not projects:
            print("No projects to save to SQL database.")
            return

        # db = self.SessionLocal()
        try:
            for project_entity in projects:
                # Conceptual: Convert Project dataclass to ProjectModel ORM object
                # db_project = ProjectModel(
                #     id=project_entity.id,
                #     name=project_entity.name,
                #     created_at=project_entity.created_at,
                #     last_updated_at=project_entity.last_updated_at,
                #     is_completed=project_entity.is_completed
                # )
                # db.merge(db_project) # merge handles insert or update

                # for task_entity in project_entity.tasks:
                #     # Conceptual: Convert Task dataclass to TaskModel ORM object
                #     db_task = TaskModel(
                #         id=task_entity.id,
                #         name=task_entity.name,
                #         duration=task_entity.duration,
                #         is_completed=task_entity.is_completed,
                #         last_updated_at=task_entity.last_updated_at,
                #         project_id=task_entity.project_id # Essential foreign key
                #     )
                #     db.merge(db_task)
                pass # Placeholder for actual DB operations

            # db.commit()
            print("Data conceptually saved to SQL database. (Actual ORM/DB-API implementation needed)")
        except Exception as e:
            # db.rollback()
            print(f"Error saving to SQL database: {e}")
        finally:
            # db.close()
            pass