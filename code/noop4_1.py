#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import inspect


def divide(a: float, b: float) -> float:
    return a / b


def check_function_types(func):
    """
    Проверяет аннотации типов функции и сравнивает их с реальными типами аргументов
    """
    print(f"Проверка функции: {func.__name__}")
    print("-" * 40)

    # Получаем сигнатуру функции
    sig = inspect.signature(func)

    # Получаем аннотации функции
    annotations = func.__annotations__

    print("Информация из inspect.signature():")
    print(f"  Сигнатура: {sig}")

    if annotations:
        print(f"  Аннотации: {annotations}")
    else:
        print("  Аннотации: отсутствуют")
        return

    print("\nПараметры функции:")
    for param_name, param in sig.parameters.items():
        param_info = f"  {param_name}: "

        # Получаем аннотацию типа
        if param.annotation != inspect.Parameter.empty:
            param_info += f"аннотация = {param.annotation.__name__}"
        else:
            param_info += "аннотация отсутствует"

        # Информация о параметре
        if param.default != inspect.Parameter.empty:
            param_info += f", значение по умолчанию = {param.default}"

        print(param_info)

    # Информация о возвращаемом значении
    if "return" in annotations:
        print(f"\nВозвращаемое значение: аннотация = {annotations['return'].__name__}")
    else:
        print("\nВозвращаемое значение: аннотация отсутствует")

    print("\n" + "=" * 40)


def test_function_with_arguments(func, test_cases):
    """
    Тестирует функцию с различными аргументами и проверяет типы
    """
    print("Тестирование функции с различными аргументами:")
    print("-" * 40)

    sig = inspect.signature(func)
    annotations = func.__annotations__

    for i, (args, kwargs) in enumerate(test_cases, 1):
        print(f"\nТест {i}:")
        print(f"  Аргументы: {args}")

        try:
            # Вызываем функцию
            result = func(*args, **kwargs)
            print(f"  Результат: {result}")
            print(f"  Тип результата: {type(result).__name__}")

            # Сравниваем с аннотацией
            if "return" in annotations:
                expected_type = annotations["return"]
                actual_type = type(result)

                # Проверяем, соответствует ли тип аннотации
                if isinstance(result, expected_type):
                    print(
                        f"  ✓ Тип результата ({actual_type.__name__}) соответствует аннотации ({expected_type.__name__})"
                    )
                else:
                    print(
                        f"  ✗ Тип результата ({actual_type.__name__}) НЕ соответствует аннотации ({expected_type.__name__})"
                    )

        except Exception as e:
            print(f"  Ошибка при выполнении: {e}")

    print("=" * 40)


if __name__ == "__main__":
    # Проверяем функцию divide
    check_function_types(divide)

    # Тестовые случаи для функции divide
    test_cases = [
        ((10, 2), {}),  # оба int
        ((10.5, 2.5), {}),  # оба float
        ((10, 2.5), {}),  # int и float
        ((10.5, 2), {}),  # float и int
        ((0, 5), {}),  # ноль в числителе
        ((10, 0), {}),  # деление на ноль (будет ошибка)
    ]

    test_function_with_arguments(divide, test_cases)

    # Дополнительная информация о модуле inspect
    print("\nДополнительная информация о функции через inspect:")
    print("-" * 40)

    # Получаем исходный код функции
    try:
        source = inspect.getsource(divide)
        print("Исходный код функции:")
        print(source)
    except:
        print("Не удалось получить исходный код")

    # Получаем информацию о модуле
    module = inspect.getmodule(divide)
    print(f"\nМодуль функции: {module}")

    # Получаем информацию о строке определения
    line_no = inspect.getsourcelines(divide)[1]
    print(f"Номер строки определения: {line_no}")

    print("\n" + "=" * 40)
    print("Проверка завершена!")
