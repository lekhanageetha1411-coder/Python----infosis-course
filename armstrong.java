public class armstrong {
    public static void main(String[] args) {
        int n = 1345;
        int output = 0;
        int last = 0;
        int arm = n;
        int sum = 0;
        while(n != 0){
            last = n %10;
            sum += (last)*last*last*last;
            n = n/10;
        }
        if(arm == sum){
            System.out.println("Armstrong value:");
        }
        else{
            System.out.println("Not an Armstrong value:");
        }

    }
}
    

