import Button from "../components/Button";

function Index() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-neutral-50 dark:bg-neutral-900">
      <div className="text-center">
        <h1 className="text-4xl font-bold text-primary dark:text-white mb-4">
          Hello World
        </h1>
        <p className="text-lg text-neutral-600 dark:text-neutral-400 mb-6">
          Welcome to your React app
        </p>
        <Button onClick={() => alert("Button clicked!")}>Click me</Button>
      </div>
    </div>
  );
}

export default Index;
