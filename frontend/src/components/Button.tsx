interface ButtonProps {
  children: React.ReactNode;
  onClick?: () => void;
  variant?: "primary" | "secondary";
  disabled?: boolean;
}

function Button({
  children,
  onClick,
  variant = "primary",
  disabled = false,
}: ButtonProps) {
  const baseStyles =
    "px-6 py-2 rounded-lg font-medium transition-colors duration-200";
  const variantStyles = {
    primary:
      "bg-primary text-white hover:bg-primary/90 active:bg-primary/80 dark:bg-white dark:text-primary dark:hover:bg-neutral-100 dark:active:bg-neutral-200",
    secondary:
      "bg-neutral-200 text-neutral-800 hover:bg-neutral-300 active:bg-neutral-400 dark:bg-neutral-700 dark:text-neutral-200 dark:hover:bg-neutral-600 dark:active:bg-neutral-500",
  };
  const disabledStyles = "opacity-50 cursor-not-allowed";

  return (
    <button
      className={`${baseStyles} ${variantStyles[variant]} ${
        disabled ? disabledStyles : ""
      }`}
      onClick={onClick}
      disabled={disabled}
    >
      {children}
    </button>
  );
}

export default Button;
