"""fill table

Revision ID: 83f3aae9aaac
Revises: 0c37eaa5b5d8
Create Date: 2025-04-04 10:32:18.897439

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from sqlalchemy.orm import Session
from domain import world_weather, heavenly_bodies

# revision identifiers, used by Alembic.
revision: str = '83f3aae9aaac'
down_revision: Union[str, None] = '0c37eaa5b5d8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    bind = op.get_bind()
    session = Session(bind = bind)
    data_h = session.query(world_weather.id, world_weather.sunrise, world_weather.sunset, world_weather.moonrise, world_weather.moonset).all()

    for i in data_h:
        session.add(
        heavenly_bodies(
            id = i.id,
            sunrise = i.sunrise,
            sunset = i.sunset,
            moonrise = i.moonrise,
            moonset = i.moonset
        )
    )

    session.commit()
    session.close()


def downgrade() -> None:
    """Downgrade schema."""
    bind = op.get_bind()
    session = Session(bind = bind)

    session.query(heavenly_bodies).delete()

    session.commit()
    session.close()
