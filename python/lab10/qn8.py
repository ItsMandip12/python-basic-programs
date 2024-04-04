class employe:
    def __init__ (self,empID,EmpName):
        self.empID=empID
        self.EmpName=EmpName
    def show(self):
        print(f"Employe ID: {self.empID}")
        print(f"Employe Name: {self.EmpName}")
class student:
    def __init__ (self,sID,sName):
        self.sID=sID
        self.sName=sName
    def show(self):
        print(f"Employe ID: {self.sID}")
        print(f"Employe Name: {self.sName}")
class person(employe,student):
    def __init__ (self,pID,pName):
        self.pID=pID
        self.pName=pName
        pass
    def show(self):
        pass