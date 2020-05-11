# Rotating Vectors Using Quaternions

We use vectors for defining the position of an object in 3D space, and quaternions for defining their rotation. Let's say the rotation of object **A** is defined by quaternion **q**, and we want to rotate this object by quaternion **r**. Calculation is very easy, all you have to do is multiply them:

    q' = q * r;

If we wanted to rotate this **A** object by **r** first and then **s**, all we had to do is multiply them in this order:

    q' = q * r * s;

or,

    t = r * s;
    q' = q * t;

However, as you might already figured out, rotating an object by **r** first then **s**, is not the same as rotating it by **s** first then **r**. It's because quaternion multiplication is not commutative:

    r * s != s * r

We can also rotate vectors using quaternions and it is very similar to rotating a quaternion: just multiply them. However, due to matrix multiplication conflict, vector should be on the right side of the multiplication. Let's say we are rotating vector **v** by quaternion **r**:

    v' = r * v;