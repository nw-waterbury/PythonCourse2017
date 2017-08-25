engine = sqlalchemy.create_engine('sqlite:////Users/nicholaswaterbury/Desktop/town.db', echo=True)

Base = declarative_base()

# Schemas
class Region(Base):
  __tablename__ = 'regions'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  departments = relationship("Department")

  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return "<Region('%s')>" % self.id

class Department(Base):
  __tablename__ = 'departments'

  id = Column(Integer, primary_key=True)
  deptname = Column(String)
  region_id = Column(Integer, ForeignKey('regions.id'))
  towns = relationship("Town")

  def __init__(self, deptname):
    self.deptname = deptname

  def __repr__(self):
    return "<Department('%s')>" % self.id

class Town(Base):
  __tablename__ = 'towns'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  population = Column(Integer)
  dept_id = Column(Integer, ForeignKey('departments.id'))

  def __init__(self, name, population):
    self.name = name
    self.population = population

  def __repr__(self):
    return "<Town('%s')>" % (self.name)

class Distance(Base):
  __tablename__ = 'distances'

  id = Column(Integer, primary_key=True)
  towndepart = Column(String, ForeignKey('towns.name'))
  townarrive = Column(String, ForeignKey('towns.name'))
  # could also use id's
  distance = Column(Integer)

  td = relationship("Town",
    primaryjoin= towndepart == Town.name)
  ta = relationship("Town",
    primaryjoin = townarrive == Town.name)

  def __init__(self, distance):
    self.distance = distance

  def __repr__(self):
    return "<Distance('%s', '%s', '%s')>" % (self.towndepart, self.townarrive, self.distance)



#First time create tables
Base.metadata.create_all(engine)

#Create a session to actually store things in the db
Session = sessionmaker(bind=engine)
session = Session()

# Create regions
reg1 = Region('Region 1')
reg2 = Region('Region 2')
reg3 = Region('Region 3')
session.add_all([reg1, reg2, reg3])

# Create departments, nested in regions
dept1 = Department('Department 1')
reg1.departments.append(dept1)

dept2 = Department('Department 2')
reg1.departments.append(dept2)

dept3 = Department('Department 3')
reg3.departments.append(dept3)

dept4 = Department('Department 4')
reg2.departments.append(dept4)

session.add_all([dept1, dept2, dept3, dept4])

# TODO: Create towns, nested in departments
a = Town("a", 1500)
dept1.towns.append(a)

b = Town("b", 110000)
dept1.towns.append(b)

c = Town("c", 501)
dept2.towns.append(c)

d = Town("d", 1000000000)
dept2.towns.append(d)

e = Town("e", 400000)
dept3.towns.append(e)

f = Town("f", 650000)
dept4.towns.append(f)

session.add_all([a,b,c,d,e,f])

ae = Distance(50)
ae.td, ae.ta = a, e

af = Distance(60)
af.td, af.ta = a, f

bc = Distance(50)
bc.td, bc.ta = b, c

bd = Distance(60)
bd.td, bd.ta = b, d

cb = Distance(50)
cb.td, cb.ta = c, b

db = Distance(60)
db.td, db.ta = d, b

de = Distance(30)
de.td, de.ta = d, e

ea = Distance(50)
ea.td, ea.ta = e, a

eb = Distance(60)
eb.td, eb.ta = e, b

ed = Distance(30)
ed.td, ed.ta = e, d

ef = Distance(100)
ef.td, ef.ta = e, f

fa = Distance(60)
fa.td, fa.ta = f, a

session.add_all([ae, af, bc, bd, cb, db, de, ea, eb, ed, ef, fa])

session.commit()

# Some example querying
for town in session.query(Town).order_by(Town.id):
  print town.name, town.population

# TODO:
# 1. Display, by department, the cities having more than 100000 inhabitants.
for city in session.query(Town).filter(Town.population > 100000):
  print "Department %s, City %s, Population %s " % (city.dept_id, city.name, city.population)
# 2. Display the list of all the one-way connections between two cities for which the population of one of the 2 cities is lower than 80000 inhabitants.
for city, dist in session.query(Town, Distance).filter(Town.population < 80000).filter(or_(Town.name == Distance.towndepart, Town.name == Distance.townarrive)):
  print dist.towndepart, dist.townarrive
# 3. Display the number of inhabitants per department (bonus: do it per region as well).
# hint: use func.sum
for dept in session.query(Department):
  deptpop = 0
  for town in session.query(Town):
    if town in dept.towns:
      deptpop += town.population
  print deptpop