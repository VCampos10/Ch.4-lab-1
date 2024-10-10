def test_powers_0f_two():
   
        N = int(input('Enter a number for N '))
        result = [0] * (N + 1)
        pow = 1

        for i in range (N + 1):
            result[i] = pow
            pow *= 2


        print (result) 



##if __name__ == '__main__':
  ##  main()