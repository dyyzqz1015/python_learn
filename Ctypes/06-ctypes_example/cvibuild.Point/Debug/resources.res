        ��  ��                  �       �� ��     0 	        <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0" />|      �� ��     0 	        |4   V S _ V E R S I O N _ I N F O     ���                 ?                        �   S t r i n g F i l e I n f o   �   0 4 0 9 0 4 b 0        C o m p a n y N a m e     L   F i l e D e s c r i p t i o n     P o i n t   ( D e b u g   x 8 6 )   (   F i l e V e r s i o n     1 . 0   ,   I n t e r n a l N a m e   P o i n t   F   L e g a l C o p y r i g h t   C o p y r i g h t       2 0 1 8     < 
  O r i g i n a l F i l e n a m e   P o i n t . d l l   .   P r o d u c t N a m e       P o i n t     ,   P r o d u c t V e r s i o n   1 . 0   D    V a r F i l e I n f o     $    T r a n s l a t i o n     	��  X   C V I D L L P R O T O T Y P E S   C V I D L L E X P O R T S         0 	        float add_float(float a, float b) __declspec(dllexport);
int add_float_ref(float *a, float *b, float *c) __declspec(dllexport);
int add_int(int a, int b) __declspec(dllexport);
int add_int_array(int *a, int *b, int *c, int n) __declspec(dllexport);
float area(struct _rect rect) __declspec(dllexport);
int getAnEnumValue(MyEnum anEnum) __declspec(dllexport);
Point get_default_point() __declspec(dllexport);
Point get_point(int x, int y) __declspec(dllexport);
Point_float get_point_float(float x, float y) __declspec(dllexport);
void move_point(Point point) __declspec(dllexport);
void move_point_by_ref(Point *point) __declspec(dllexport);
void show_point(Point point) __declspec(dllexport);
          �� ��     0	                                        