# Linear-Algebra-project
A project utilizing linear algebra and matrix math to perform image transformations using python matplotlib   
This project was submitted for the linear algebra course in Alexandria university Faculty of engineering

# The first Question:  
**Rotation, Scaling & Reflection**   
We need to determine two linear transformations, $$𝑭_𝟏(𝑿) = 𝑩_𝟏 𝑿 and 𝑭𝟐(𝑿) = 𝑩_𝟐S$$, where 𝑩𝟏 is the matrix that produces the first
transformed image from the original, and 𝑩𝟐 is the matrix that achieves the second transformation from the original image as
shown in figure 1   

<img width="836" height="408" alt="image" src="https://github.com/user-attachments/assets/9e29c636-1e81-4fbf-9b41-fc0f0dd0eaf3" />

# Second Question:
**Translation, Scaling and Reflection**   
Linear maps F(X) = BX, where “B” is a transformation matrix, have the property that F(0)=0, so they necessarily leave the origin fixed.
It is simple to extend this to include a transition, F(X) = V + BX, where V is a vector. Note that F(0)=V. Find the vector V and the
matrix B that describe the following mapping (here the black shape is transformed to the red one) as shown in Figure (2).

<img width="575" height="421" alt="image" src="https://github.com/user-attachments/assets/c5e0a200-d383-4c70-8d4b-5b838487cf56" />   

# Solutions:

## First Question:   
In order to determine the transformation matrix for a given operation, 
we take 2 vectors and form a $2\times2$ matrix then find their inverse and multiply it by the transformed vector matrix to find the transformation matrix.     
$`
\begin{equation}
\begin{bmatrix}
a' & b'\\    
c' & d'
\end{bmatrix} = B \cdot
\begin{bmatrix}
a & b\\    
c & d
\end{bmatrix}
\end{equation}
`$     




$`
\begin{equation}
\begin{bmatrix}
a' & b'\\    
c' & d'
\end{bmatrix}
\cdot
\begin{bmatrix}
a & b\\    
c & d
\end{bmatrix}^{-1} = B
\end{equation}
`$     
Therfore we use any 2 independent vectors and their transformed versions to find the transformation matrix and get:    
$`
\textbf{First transformation: }
\boxed{B_1 =\begin{bmatrix}
-0.5 & 0\\
0 & 0.5
\end{bmatrix}}
`$     

      

$`
\textbf{Second transformation: }
\boxed{B_2 =\begin{bmatrix}
0 & -0.5\\
-0.5 & 0
\end{bmatrix}}
`$    

<img width="623" height="576" alt="Screenshot from 2026-01-11 13-55-57" src="https://github.com/user-attachments/assets/40c55c10-2f6e-4035-a4b7-52a2ca604c66" />    


## Second Question:
We form a general equation for the transformation and the translation and convert it to a system of linear equations and solve for each unknown variable.    

$`   
\begin{equation}
\begin{bmatrix}
a'\\    
b'\\
\end{bmatrix} = B
\begin{bmatrix}
a\\    
b\\
\end{bmatrix} + 
\begin{bmatrix}
x\\
y
\end{bmatrix}
\end{equation}
`$     
After simplifying we get:     
$`     
\begin{equation}
a' = B_{11}a + B_{12}b + x \newline
\end{equation}
`$     
$`    
\begin{equation}
b' = B_{21}a + B_{22}b + y
\end{equation}
`$     
We can then form a $3\times3$ system of linear equations to solve for the unknowns in the transformation matrix     
$`     
\textbf{Transformation matrix:}
\boxed{B =\begin{bmatrix}
\frac{1}{4} & 0\\    
0 & -2
\end{bmatrix}}
`$   
     
     
     
$` 
\textbf{Translation vector:}
\boxed{V = \begin{bmatrix}
5\\    
0
\end{bmatrix}}
`$      
<img width="1109" height="580" alt="Screenshot from 2026-01-11 13-56-27" src="https://github.com/user-attachments/assets/e25cd77f-268e-430c-a006-8be3faf3d5ea" />  


