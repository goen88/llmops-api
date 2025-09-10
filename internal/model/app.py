import uuid
from datetime import datetime

from sqlalchemy import (
    Column, UUID, DateTime, Text, String,
    PrimaryKeyConstraint, Index
)

from internal.extension.database_extension import db


class App(db.Model):
    '''AI应用基础类'''
    __tablename__ = 'app'
    __table_args__ = (
        PrimaryKeyConstraint('id',name='pk_app_id'),
        Index('idx_app_account_id', 'account_id')
    )

    id = Column(UUID, default=uuid.uuid4, nullable=False)
    account_id = Column(UUID, nullable=False)
    name = Column(String(255), nullable=False)
    icon = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def to_dict(self):
        return {
            'id': str(self.id),
            'account_id': str(self.account_id),
            'name': self.name,
            'icon': self.icon,
            'description': self.description,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        }