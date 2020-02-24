
# Expression programming


class Computer(object):

    NAME = None;


    def GetName(self):
        return self.NAME;
    
    def SetName(self, name):
        Computer.NAME  =  name;



c =  Computer();

c.SetName("Obaro");

d = Computer();
d.SetName("Isreal");

print(d.GetName());
print(c.GetName())
