"""initial database migration

Revision ID: 6a263a45a174
Revises: 
Create Date: 2018-10-28 12:41:57.302036

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a263a45a174'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(length=255), nullable=False),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.Column('prenoms', sa.String(length=50), nullable=True),
    sa.Column('date_naissance', sa.String(length=50), nullable=True),
    sa.Column('situation_matrimoniale', sa.String(length=50), nullable=True),
    sa.Column('entreprise', sa.String(length=50), nullable=True),
    sa.Column('longitude', sa.Numeric(precision=8, asdecimal=False), nullable=True),
    sa.Column('latitude', sa.Numeric(precision=8, asdecimal=False), nullable=True),
    sa.Column('forme_juridique', sa.String(length=50), nullable=True),
    sa.Column('adresse', sa.String(length=50), nullable=True),
    sa.Column('fonction', sa.String(length=50), nullable=True),
    sa.Column('dom_activite', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('adresse'),
    sa.UniqueConstraint('date_naissance'),
    sa.UniqueConstraint('dom_activite'),
    sa.UniqueConstraint('entreprise'),
    sa.UniqueConstraint('fonction'),
    sa.UniqueConstraint('forme_juridique'),
    sa.UniqueConstraint('nom'),
    sa.UniqueConstraint('prenoms'),
    sa.UniqueConstraint('situation_matrimoniale')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('client')
    # ### end Alembic commands ###
