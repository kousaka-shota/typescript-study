export const Practice1 = () => {
  const calculate = (num: number) => {
    console.log(num ** 2);
  };
  const onClickPractice = () => calculate(100);
  return (
    <div>
      <p>練習</p>
      <button onClick={onClickPractice}>練習問題を実行</button>
    </div>
  );
};
