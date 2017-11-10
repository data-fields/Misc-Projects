namespace TestSet
{
  public class Test
  {
    Object[] elements = new Object[10];
    int size = 0;
    
    public boolean isempty(){
      return size == 0;
    }
    
    public int getsize(){
      return size;
    }
    
    public void addElement(Object o){
      if (indexOf(o) < 0){
      if (size +1 > elements.Length){
      size * = 2;
      Object[] temp = new Object[size];
      Array.Copy(elements,temp,elements.length);
      elements = temp;
      }
      elements[size] = o;
        size++;
      }
    }
    
    public void removeElement(Object o){
      int index = indexOf(o);
      if (index >= 0){
        elements[index] = elements[size - 1];
        size --;
      }
    }
    public boolean contains(Object o){
      return indexOf(o) >= 0; 
    }
    
    private int indexOf(Object o){
      for int( i = 0; i<size; i++){
        if (elements[i].Equals(o)){
          return i
        }
      }
      return -1
    }
  }
}

          