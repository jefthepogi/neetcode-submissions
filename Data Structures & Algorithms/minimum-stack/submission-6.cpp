class MinStack {
public:
    std::stack<int> main;
    std::stack<int> min;

    MinStack() {
        
    }
    
    void push(int val) {
        main.push(val);
        if (min.empty() || val <= min.top())
            min.push(val);
    }
    
    void pop() {
        if (main.top() == min.top())
            min.pop();
        main.pop();
    }
    
    int top() {
        return main.top();
    }
    
    int getMin() {
        return min.top();
    }
};
