"""init

Revision ID: 60c95cb681f7
Revises: 53754b2c08a4
Create Date: 2024-05-23 06:29:05.725574

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '60c95cb681f7'
down_revision = '53754b2c08a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_song_artist', table_name='song')
    op.drop_index('ix_song_id', table_name='song')
    op.drop_index('ix_song_name', table_name='song')
    op.drop_index('ix_song_year', table_name='song')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_song_year', 'song', ['year'], unique=False)
    op.create_index('ix_song_name', 'song', ['name'], unique=False)
    op.create_index('ix_song_id', 'song', ['id'], unique=False)
    op.create_index('ix_song_artist', 'song', ['artist'], unique=False)
    # ### end Alembic commands ###
