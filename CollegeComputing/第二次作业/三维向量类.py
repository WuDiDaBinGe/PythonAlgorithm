class Vector3D:
    epsilon = 1.0e-6

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        t_x,t_y,t_z = 0,0,0
        if isinstance(other,Vector3D):
            t_x = other.x
            t_y = other.y
            t_z = other.z
        else:
            t_x = other[0]
            t_y = other[1]
            t_z = other[2]
        return Vector3D(t_x+self.x,t_y+self.y,t_z+self.z)

    def __radd__(self, other):
        t_x, t_y, t_z = 0, 0, 0
        if isinstance(other, Vector3D):
            t_x = other.x
            t_y = other.y
            t_z = other.z
        else:
            t_x = other[0]
            t_y = other[1]
            t_z = other[2]
        return Vector3D(t_x + self.x, t_y + self.y, t_z + self.z)

    def __sub__(self, other):
        t_x, t_y, t_z = 0, 0, 0
        if isinstance(other, Vector3D):
            t_x = other.x
            t_y = other.y
            t_z = other.z
        else:
            t_x = other[0]
            t_y = other[1]
            t_z = other[2]
        return Vector3D(-t_x + self.x, -t_y + self.y, -t_z + self.z)

    def __rsub__(self, other):
        t_x, t_y, t_z = 0, 0, 0
        if isinstance(other, Vector3D):
            t_x = other.x
            t_y = other.y
            t_z = other.z
        else:
            t_x = other[0]
            t_y = other[1]
            t_z = other[2]
        return Vector3D(t_x - self.x, t_y - self.y, t_z - self.z)

    def __mul__(self, other):
        t_x, t_y, t_z = 0, 0, 0
        if isinstance(other, Vector3D):
            t_x = other.x
            t_y = other.y
            t_z = other.z
        else:
            t_x = other[0]
            t_y = other[1]
            t_z = other[2]
        return Vector3D(t_x * self.x, t_y * self.y, t_z * self.z)

    def __rmul__(self, other):
        t_x, t_y, t_z = 0, 0, 0
        if isinstance(other, Vector3D):
            t_x = other.x
            t_y = other.y
            t_z = other.z
        else:
            t_x = other[0]
            t_y = other[1]
            t_z = other[2]
        return Vector3D(t_x * self.x, t_y * self.y, t_z * self.z)

    def __eq__(self, other):
        if isinstance(self.x, float) or isinstance(other.x, float):
            e1 = abs(self.x - other.x) < self.epsilon
            e2 = abs(self.y - other.y) < self.epsilon
            e3 = abs(self.z - other.z) < self.epsilon
            return e1 and e2 and e3
        else:
            print(self.x , other.x)
            print(self.y , other.y)
            print(self.z , other.z)
            return self.x == other.x and self.y == other.y and self.z == other.z

    def __str__(self):
        return "<%g, %g, %g>" % (self.x, self.y, self.z)



def tVector3D(vec1, vec2, vec3, vec4):
    vec1 = Vector3D(vec1[0], vec1[1], vec1[2])
    vec2 = Vector3D(vec2[0], vec2[1], vec2[2])
    print("%s + %s = %s" % (vec1, vec2, vec1 + vec2))
    print("%s - %s = %s" % (vec1, vec2, vec1 - vec2))
    print("%s * %s = %s" % (vec1, vec2, vec1 * vec2))

    print("%s + %s = %s" % (vec1, vec3, vec1 + vec3))
    print("%s - %s = %s" % (vec1, vec3, vec1 - vec3))
    print("%s * %s = %s" % (vec1, vec3, vec1 * vec3))

    print("%s + %s = %s" % (vec4, vec2, vec4 + vec2))
    print("%s - %s = %s" % (vec4, vec2, vec4 - vec2))
    print("%s * %s = %s" % (vec4, vec2, vec4 * vec2))

    vec5 = vec1 + vec4
    if (vec1 == vec5):
        print("%s is equal to %s" % (vec1, vec5))
    else:
        print("%s not equal to %s" % (vec1, vec5))

tVector3D([1, 2, 3] ,[2.2, 7.7, 9.9] ,[-1, -2, 0] ,(0.0000001, 0.0000001, 0.0000001))

