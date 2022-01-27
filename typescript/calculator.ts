// Useful for styling dynamic components' sizes
function px(x: number) { return (x * this.props.viewScale)+'px'; };

//== Evaluation algorithm ==//

function evaluate() {
   //-- Checking for valid input --//
  
  let errorMessage: string;
  
  //-- Checking for errors in entering numbers
  
  let numberError: boolean = false;
  
  // Combining numbers and decimal points
  let input: any[];
  input = this.state.in.reduce((prev: string[], curr: string, index: number) => {
    if( parseInt(curr) == curr
        && index !== 0
        && ( prev[prev.length-1] === "."
             || prev[prev.length-1] == parseFloat(prev[prev.length-1]) ) ) {
      prev[prev.length-1] += curr;
    }
    else if( curr === "."
             && index !== 0
             && prev[prev.length-1].indexOf(".") === -1
             && prev[prev.length-1] == parseFloat(prev[prev.length-1]) ) {
      prev[prev.length-1] += curr;
    }
    else prev.push(curr);
    return prev;
  }, []);
  numberError = input.reduce((prev: string, curr: string, index: number) => {
    if(prev) return prev;
    
    // Checks for extra decimal points
    if( curr === "." ) {
      errorMessage = "Error: Unexpected \""+ curr +"\"";
      return true;
    }
    // Makes sure no negative sign at the end of the input
    if( input[input.length-1] === "-" ) {
      errorMessage = "Error: Unexpected \"-\"";
      return true;
    }
    // Check if there is a negative sign next to an illegal character
    else if( curr === "-" 
             && input[index+1] !== "("
             && input[index+1] != parseFloat(input[index+1]) ) {
      errorMessage = "Error: Unexpected \"-\"";
      return true;
    }
    // Check for consecutive numbers with no operator between them
    if( curr == parseFloat(curr)
        && index !== 0
        && input[index-1] == parseFloat(input[index-1]) ) {
      errorMessage = "Error: Unexpected num"
      return true;
    }
    
    return prev;
  }, numberError);
  if(numberError) {
    this.state.out = errorMessage;
    return;
  }
  
  //-- Operator errors
  
  let operatorError: boolean;
  let isOperator: (s: string) => boolean;
  
  // Checking to make sure all arithmetic operators
  // are used correctly
  isOperator = (s: string) => {
    return ( s == '+' 
             || s == '='
             || s == '*'
             || s == '/'
             || s == '^' )
  }
  operatorError = input.reduce(( prev:  string, 
                         elem:  string,
                         index: number ) => {
    // Operators cannot be the first char in the input
    if( isOperator(elem) ) {
      // The input cannot start or end with an operator
      if( index === 0 || index === input.length-1 ) {
        errorMessage = "Error: Unexpected \"" + (elem==="="? '-':elem) + '\"';
        return true;
      }
      // Operators' left neighbor needs to be a number
      // or a closed parenthesis
      if( parseFloat(input[index-1]) != input[index-1]
          && input[index-1] !== ")" ) {
        errorMessage = "Error: Unexpected \""+ (elem==="="? '-':elem) +"\"";
        return true
      }
      // Operators' right neighbor needs to be a number,
      // an open parenthesis, or a negative sign
      if( parseFloat(input[index+1]) != input[index+1]
          && input[index+1] !== "("
          && input[index+1] !== "-" ) {
        errorMessage = "Error: Expected num or \"(\"";
        return true
      }
    }
    
    return prev;
  }, false);
  if(operatorError) {
    this.state.out = errorMessage;
    return;
  }
  
  //-- Checking for parenthesis errors
  
  let depth: number;
  let inputStr: string[];
  
  depth = 0;
  for(var i = 0; i < input.length; i++) {
    depth += input[i] === "("? 1
             : input[i] === ")"? -1 : 0;
    // Check for empty parentheses
    if( input[i] === ")"
        && i !== 0
        && input[i-1] === "(" ) {
      this.state.out = "Error: Empty parens";
      return;
    }
    // Check to make sure close parenthesis are followed
    // by an operator
    if( input[i] === ")"
        && i !== input.length-1
        && !isOperator(input[i+1]) ) {
      this.state.out = "Error: Expected operator "+i;
      return;
    }
    // Check to make sure open parenthesis are preceded
    // by an operator or a negative sign
    if( input[i] === "("
        && i != 0 
        && !isOperator(input[i-1])
        && input[i-1] !== "-" )  {
      this.state.out = "Error: Unexpected \"(\"";
      return;
    }
  }
  
  if(depth > 0) {
    this.state.out = "Error: Unmatched \"(\"";
    return;
  }
  if(depth < 0) {
    this.state.out = "Error: Unexpected \")\"";
    return;
  }
  
  this.state.out = '' + evaluateInOrder.call(this, input);
  //-- End of checking for valid input --//
} // End of the evaluate function

// Evaluates in-order arithmetic expression
// by converting it to post-fix
function evaluateInOrder(input: any[]): number {
  input = input.reduce(( prev:  any,    curr: any,
                         index: number, arr: any[]) => {
    if(curr === '(') {
      arr.splice(index, 1);
      
      let depth: number;
      let parenExp: any[];
      
      depth = 1;
      parenExp = [];
      
      while( depth !== 0 ) {    
        if( arr[index] === '(' ) depth++;
        if( arr[index] === ')' ) depth--;
        if(depth) {
          parenExp.push(arr[index]);
          arr.splice(index, 1);
        }
      }
      
      prev.push(evaluateInOrder(parenExp));
    }
    else prev.push(curr);
    return prev;
  }, []);
  
  let postfix: any[];
  let stack: string[];
  
  // Converting numerical strings to number objects
  input = input.map((curr: string) =>
    curr == parseFloat(curr)? parseFloat(curr) : curr
  );
  // Combining negative signs with numbers
  input = input.reduce(( prev:  string[], curr: string,
                         index: number,   arr: string[] ) => {
    if(curr === '-') {
      curr = -1 * arr[index+1];
      arr.splice(index+1, 1);
    }
    
    prev.push(curr);
    return prev;
  }, []);
  
  // Expression conversion
  postfix = [];
  stack = [];
  input.map((curr: string, index: number) => {
    if( !isNaN(curr) ) {
      postfix.push(curr);
      return;
    }
    
    if( !stack.length ) {
      stack.push(curr);
    }
    else if( stack.length ) {
      if( curr === '+' || curr === '=' ) {
        while( stack.length
               && stack[stack.length-1] !== '+'
               && stack[stack.length-1] !== '=' ) postfix.push(stack.pop());
        stack.push(curr);
      }
      else if( curr === '*' || curr === '/' ) {
        while( stack.length
               && stack[stack.length-1] !== '+'
               && stack[stack.length-1] !== '='
               && stack[stack.length-1] !== '*'
               && stack[stack.length-1] !== '/' ) postfix.push(stack.pop());
        stack.push(curr);
      }
      else if( curr === '^' ) {
        while( stack.length
               && stack[stack.length-1] !== '+'
               && stack[stack.length-1] !== '='
               && stack[stack.length-1] !== '*'
               && stack[stack.length-1] !== '/'
               && stack[stack.length-1] !== '^' ) postfix.push(stack.pop());
        stack.push(curr);
      }
    }
  });
  while(stack.length) postfix.push(stack.pop());
  
  // Evaluating the postfix string
  let output: number;
  postfix.map((curr: any) => {
    if( !isNaN(curr) ) {
      stack.push(curr);
    }
    else {
      let temp: number;
      temp = stack.pop();
      if( curr === '+' ) temp += stack.pop();
      if( curr === '=' ) temp = stack.pop() - temp;
      if( curr === '*' ) temp *= stack.pop();
      if( curr === '/' ) temp = stack.pop() / temp;
      if( curr === '^' ) temp = Math.pow(stack.pop(), temp);
      stack.push(temp);
    }
  });
  output = stack.pop();
  
  if( Math.abs(output) < 1e-5 ) {
    return (Math.round(output * 1e6) / 1e6).toExponential();
  }
  else if( Math.abs(output) > 1e7 ) {
    return  (Math.round(output * 1e6) / 1e6).toExponential();
  }
  else{
    return Math.round(output * 1e6) / 1e6;
  }
}

//== Adding and deleting inputs ==//

function addInput(s: string) {
  this.state.in.push(s);
  this.state.out = '';
}
function delInput(all: boolean) {
  if(all) {
    this.state.in = [];
    this.state.out = '';
  }
  else {
    this.state.in.pop();
    this.state.out = '';
  }
}

//-- REACT COMPONENTS --//

interface CalcProps {
  viewScale: number;
}
interface CalcState {
  in: string[];
  out: string;
}
class Calculator extends React.Component<CalcProps, CalcState> {
  public evaluate: () => void;
  public addInput: (s: string) => void;
  public delInput: (all: boolean) => void;
  
  constructor() {
    super();
    this.state = { in:  [],
                   out: '' };
    this.evaluate = evaluate.bind(this);
    this.addInput = addInput.bind(this);
    this.delInput = delInput.bind(this);
  }
  
  renderButtons() {
    return getButtons( this.props.viewScale,
                       this.evaluate,
                       this.addInput,
                       this.delInput );
  }
  
  private containerStyle() { return {
    width: px.call(this, 400),
    left: window.innerWidth > 400 ? (window.innerWidth/2-200)+'px' : '0px',
    paddingTop: px.call(this, 40),
    paddingBottom: px.call(this, 100)
  }}
  private bodyStyle() { return {
    width: px.call(this, 300),
    height: px.call(this, 535),
    left: px.call(this, 50),
    borderRadius: px.call(this, 15)
  }}
  private headingStyle() { return {
    top: px.call(this, 5),
    fontSize: px.call(this, 25)
  }}
  private signatureStyle() { return {
    top: px.call(this, 15),
    fontSize: px.call(this, 16)
  }}
  
  public render() {
    return <div id="container" style={this.containerStyle()} >
      <div id="calculator-body" style={this.bodyStyle()}>
        <div id="calculator-heading" style={this.headingStyle()}>
          JavaScript Calculator
        </div>
        <Screen viewScale={this.props.viewScale}
                in={this.state.in}
                out={this.state.out} />
        {this.renderButtons.apply(this)}
      </div>
      <div id="signature" style={this.signatureStyle()}>
        {'Made with '}<i className="fa fa-heart" />{' by Dylan Cutler'}
      </div>
    </div>;
  }
} // End of Calculator

interface ScreenProps {
  viewScale: number;
  in: string[];
  out: any;
}
interface ScreenState {
  cursorVisible: boolean;
}
class Screen extends React.Component<ScreenProps, ScreenState> {
  constructor() {
    super();
    this.state = { cursorVisible: true };
  }
  
  containerStyle() { return {
    top: px.call(this, 45),
    left: px.call(this, 10),
    width: px.call(this, 280),
    height: px.call(this, 150),
    borderRadius: px.call(this, 5)
  }}
  inputLabelStyle() { return {
    top: px.call(this, 5),
    left: px.call(this, 5),
    width: px.call(this, 35),
    fontSize: px.call(this, 15)
  }}
  outputLabelStyle() { return {
    bottom: px.call(this, 5),
    left: px.call(this, 5),
    width: px.call(this, 35),
    fontSize: px.call(this, 15)
  }}
  inputDisplayStyle() { return {
    top: px.call(this, 5),
    left: px.call(this, 45),
    width: px.call(this, 220),
    height: px.call(this, 105),
    fontSize: px.call(this, 25),
    paddingLeft: px.call(this, 5),
    paddingRight: px.call(this, 5)
  }}
  outputDisplayStyle() { return {
    top: px.call(this, 120),
    left: px.call(this, 45),
    width: px.call(this, 220),
    height: px.call(this, 25),
    fontSize: px.call(this, 20),
    paddingLeft: px.call(this, 5),
    paddingRight: px.call(this, 5)
  }}
  cursorStyle() { return {
    color: this.state.cursorVisible?
     'rgba(30, 35, 20, 0.6)' : 'rgba(0, 0, 0, 0)'
  }}

  render() {
    return <div id="screen-container" style={this.containerStyle()}>
      <div className="screen-label" style={this.inputLabelStyle()}>
        {"In="}
      </div>
      <div className="screen-label" style={this.outputLabelStyle()}>
        {"Out="}
      </div>
      <div className="screen-display"
           id="input"
           style={this.inputDisplayStyle()}>
        {this.props.in.map((curr: string) => curr==='='? '-':curr ).join('')}
        <span style={this.cursorStyle()}>{'_'}</span>
      </div>
      <div className="screen-display"
           style={this.outputDisplayStyle()} >
        {this.props.out}
      </div>
    </div>;
  }
  componentDidMount() {
    setInterval(() => {
      var elem = document.getElementById('input');
      elem.scrollTop = elem.scrollHeight;
    }, 250);
    setInterval(() => {
      if(this.state.cursorVisible) this.state.cursorVisible = false
      else this.state.cursorVisible = true;
    }, 750);
  }
} // End of Screen component

interface ButtonProps {
  key: number;
  viewScale: number;
  x: number;
  y: number;
  width: number;
  height: number;
  content: string;
  light: boolean;
  callback: () => void;
}
class Button extends React.Component<ButtonProps, {}> {
  btnStyle() { return {
    left: px.call(this, this.props.x),
    top: px.call(this, this.props.y),
    width: px.call(this, this.props.width),
    height: px.call(this, this.props.height),
    borderRadius: px.call(this, 5),
    paddingBottom: px.call(this, 5),
    fontSize: px.call(this, 18)
  }}
  
  render() {
    let name: string;
    name = "calculator-button ";
    name += this.props.light?
      'light-button' : 'dark-button';
    return <button className={name}
                   style={this.btnStyle()}
                   onClick={this.props.callback}>
      <b>{this.props.content}</b>
    </button>;
  }
} // End of button component

// Get all buttons for calculator
function getButtons( vs:       number,
                     evaluate: () => void,
                     addInput: (s: string) => void,
                     delInput: (all: boolean) => void ) {
  let x: number[];
  let y: number[];
  let width: number[];
  let height: number[];
  let content: any[];
  let light: boolean[];
  let callback: Function[];
  
  x = [ 35, 95, 155, 215,
        35, 95, 155, 215,
        35, 95, 155, 215,
        35, 95, 155, 215,
        35, 95, 155, 215,
        35,          215 ];
  y = [ 210, 210, 210, 210,
        260, 260, 260, 260,
        310, 310, 310, 310,
        360, 360, 360, 360,
        410, 410, 410, 410,
        460,           460 ];
  width = [ 50, 50, 50, 50,
            50, 50, 50, 50,
            50, 50, 50, 50,
            50, 50, 50, 50,
            50, 50, 50, 50,
            170,         50 ];
  height = 40;
  content = [ '(',   ')', '+', '-', 
              '1',   '2', '3', <i className="fa fa-times" />,
              '4',   '5', '6', '/',
              '7',   '8', '9', '^',
              '(-)', '0', '.', 'Del',
              'Enter',         'Clr' ];
  light = [ false, false, false, false,
            true,  true,  true,  false,
            true,  true,  true,  false,
            true,  true,  true,  false,
            true,  true,  true,  false,
            false,               false ];
  callback = [ ()=>addInput('('), ()=>addInput(')'),
               ()=>addInput('+'), ()=>addInput('='),
               ()=>addInput('1'), ()=>addInput('2'),
               ()=>addInput('3'), ()=>addInput('*'),
               ()=>addInput('4'), ()=>addInput('5'),
               ()=>addInput('6'), ()=>addInput('/'),
               ()=>addInput('7'), ()=>addInput('8'),
               ()=>addInput('9'), ()=>addInput('^'),
               // Equals sign distinguishes negative signs
               // from subtraction operator
               ()=>addInput('-'), ()=>addInput('0'),
               ()=>addInput('.'), ()=>delInput(),
               ()=>evaluate(),    ()=>delInput(true) ];
  
  return x.map((curr: number, i: number) => {
    return <Button key={i}
                   viewScale={vs}
                   width={width[i]}
                   height={height}
                   x={curr} y={y[i]}
                   content={content[i]}
                   light={light[i]}
                   callback={callback[i]} />;
  });
                 
}

//-- MAIN --//

function main() {
  ReactDOM.render( <Calculator viewScale={Math.min(1, window.innerWidth/400)} />,
                   document.getElementById('root') );
  window.requestAnimationFrame(main);
}
main();
