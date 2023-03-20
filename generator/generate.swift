import Foundation

// Generator

struct Generator {
    static func generatePyVibe() -> String {
        var pythonCode: String = """
        from __future__ import annotations
        from .component_interface import *
        import uuid
        
        \n\n
        """

        // Group by attachableTo
        var attachedElements: [ElementType: [ElementType]] = [:]

        // Put all elements in the Dictionary

        for type: ElementType in ElementType.allCases {
            if attachedElements[type] == nil {
                attachedElements[type] = []
            }
        }

        for type: ElementType in ElementType.allCases {
            let element: Element = type.element

            for attachableTo: ElementType in element.attachableTo {
                attachedElements[attachableTo]!.append(type)
            }
        }

        for attachment: Dictionary<ElementType, [ElementType]>.Element in attachedElements.sorted(by: { $0.key.rawValue < $1.key.rawValue}) {
            print("attachment: \(attachment.key) -> \(attachment.value)")
            
            let classElement: Element = attachment.key.element
           // ElementType with uppercase first letter
            let classElementTypeStr: String = attachment.key.rawValue.prefix(1).uppercased() + attachment.key.rawValue.dropFirst()

            if classElement.category == .advanced {
                pythonCode += ""
            } else {
                let className: String = classElement.attachableTo.count > 0 ? "\(classElementTypeStr)Component" : "\(classElementTypeStr)"

            pythonCode += """
class \(className)(Component):
  \"""You don't normally need to invoke this constructor directly.
  
  Instead, use the `Page.add_\(attachment.key.rawValue)` method of the parent component.
  ""\"
  def __init__(\(classElement.arguments.pythonArgumentListWithDefaults())):    
    \(classElement.arguments.pythonArgumentListSelfAssignment())
    \(classElement.postInitPythonFunc?.replacingOccurrences(of: "\n", with: "\n    ") ?? "")

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''\(classElement.toTailwindHtmlTemplate(in: .pycob))'''


"""

                if classElement.arguments.contains(where: {$0.type == .elements}) {
                    pythonCode += """
                      def add(self, component):
                        self.components.append(component)
                        return self

                      def add_component(self, component):
                        self.components.append(component)
                        return self

                    """
                }
            }

            for type: ElementType in attachment.value {
                let attachedElement: Element = type.element
                // ElementType with uppercase first letter
                let attachedElementTypeStr: String = type.rawValue.prefix(1).uppercased() + type.rawValue.dropFirst()

                if attachedElement.category == .advanced {
                    pythonCode += """

  def add_\(type.rawValue)(\(attachedElement.arguments.pythonArgumentListWithDefaults())):
    \"""\(attachedElement.description)

    \(attachedElement.arguments.pythonArgumentDocString())
    
    Returns:
        \(attachedElementTypeStr)Component: The new component
    ""\"
    advanced_add_\(type.rawValue)(self, \(attachedElement.arguments.pythonArgumentListNoTypes()))
    return self
    \n\n
"""
                } else {
                pythonCode += """
  def add_\(type.rawValue)(\(attachedElement.arguments.pythonArgumentListWithDefaults())) -> \(attachedElementTypeStr)Component:
    \"""\(attachedElement.description)

    \(attachedElement.arguments.pythonArgumentDocString())
    
    Returns:
        \(attachedElementTypeStr)Component: The new component
    ""\"
    new_component = \(attachedElementTypeStr)Component(\(attachedElement.arguments.pythonArgumentListNoTypes()))    
    self.components.append(new_component)
    return new_component
    \n\n
"""
                }
            }
        }

        

        return pythonCode
    }

    static func generatePyVibeComponents() -> String {
        var pythonCode: String = ""

        pythonCode += """

        """

        for type: ElementType in ElementType.allCases {
            let classElement: Element = type.element
            // ElementType with uppercase first letter
            let classElementTypeStr: String = type.rawValue.prefix(1).uppercased() + type.rawValue.dropFirst()

            if classElement.category == .advanced {
                pythonCode += ""
            } else {
                let className: String = classElement.attachableTo.count > 0 ? "\(classElementTypeStr)Component" : "\(classElementTypeStr)"

            pythonCode += """
class \(className)(Component):
  def __init__(\(classElement.arguments.pythonArgumentListWithDefaults())):    
    \(classElement.arguments.pythonArgumentListSelfAssignment())

  def to_html(self):
    return f'''\(classElement.toTailwindHtmlTemplate(in: .pycob))'''


"""
            }
        }

        return pythonCode
    }
}

extension String {
    func makeHTMLfriendly() -> String {
        var finalString: String = ""
        for char: Character in self {
            for scalar: Unicode.Scalar in String(char).unicodeScalars {
                finalString.append("&#\(scalar.value)")
            }
        }
        return finalString
    }
}

// 

enum RenderingSystem: String, CaseIterable {
    case pycob
    case react
}

enum ElementType: String, CaseIterable, Codable {
    case page
    case html
    case text
    case link
    case plainlink
    case list
    case listitem
    case image
    case header
    case card
    case container
    case alert
    case code
    case divider
    case section
    case form
    case formtext
    case formemail
    case formpassword
    case formselect
    case formhidden
    case selectoption
    case formtextarea
    case formsubmit
    case rawtable
    case tablehead
    case tablerow
    case tablecol
    case tablebody
    case tablecell
    case tablecellheader
    case pandastable
    case plotlyfigure
    case datagrid
    case rowaction
    case navbar
    case navbarlink
    case footer
    case footercategory
    case footerlink
    case sidebar
    case sidebarcategory
    case sidebarlink
    case codeeditor
    case emgithub
    case scriptstatus

    var element: Element {
        switch self {
        case .page:
            return PageElement()
        case .html:
            return HtmlElement()
        case .text:
            return TextElement()
        case .link:
            return LinkElement()
        case .plainlink:
            return PlainLinkElement()
        case .list:
            return ListElement()
        case .listitem:
            return ListItemElement()
        case .image:
            return ImageElement()
        case .header:
            return HeaderElement()
        case .card:
            return CardElement()
        case .container:
            return ContainerElement()
        case .alert:
            return AlertElement()
        case .code:
            return CodeElement()
        case .codeeditor:
            return CodeEditorElement()
        case .emgithub:
            return EmGithubElement()
        case .divider:
            return DividerElement()
        case .section:
            return SectionElement()
        case .form:
            return FormElement()
        case .formtext:
            return FormTextElement()
        case .formemail:
            return FormEmailElement()
        case .formpassword:
            return FormPasswordElement()
        case .formselect:
            return FormSelectElement()
        case .formhidden:
            return FormHiddenElement()
        case .selectoption:
            return SelectOptionElement()
        case .formtextarea:
            return TextAreaElement()
        case .formsubmit:
            return FormSubmitElement()
        case .rawtable:
            return RawTableElement()
        case .tablehead:
            return TableHeadElement()
        case .tablerow:
            return TableRowElement()
        case .tablecol:
            return TableColElement()
        case .tablebody:
            return TableBodyElement()
        case .tablecell:
            return TableCellElement()
        case .tablecellheader:
            return TableCellHeaderElement()
        case .pandastable:
            return PandasTableElement()
        case .plotlyfigure:
            return PlotlyFigureElement()
        case .datagrid:
            return DataGridElement()
        case .rowaction:
            return RowActionElement()
        case .navbar:
            return NavbarElement()
        case .navbarlink:
            return NavbarLinkElement()
        case .footer:
            return FooterElement()
        case .footercategory:
            return FooterCategoryElement()
        case .footerlink:
            return FooterLinkElement()
        case .sidebar:
            return SidebarElement()
        case .sidebarcategory:
            return SidebarCategoryElement()
        case .sidebarlink:
            return SidebarLinkElement()
        case .scriptstatus:
            return ScriptStatusElement()
        }
    }
}

enum DocumentationCategory: String, CaseIterable, Codable {
    case basicHtml = "Basic HTML"
    case layout = "Layout"
    case form = "Form"
    case table = "Table"
    case charts = "Charts"
    case advanced = "Advanced"
    case `internal` = "Internal"
}

enum ArgumentType: String, CaseIterable, Codable {
    case int = "Integer"
    case optionalInt = "Optional Integer"
    case string = "String"
    case optionalString = "Optional String"
    case bool = "Boolean"
    case optionalBool = "Optional Boolean"
    case elements = "Components"
    case list = "List"
    case navbar = "Navbar"
    case footer = "Footer"
    case untyped = "Untyped"
}

typealias ArgumentDescription = String

typealias ArgumentName = String

struct Argument: Codable {
    var name: ArgumentName
    var type: ArgumentType
    var description: ArgumentDescription
    var defaultValue: String?

    func templateVariable(in renderingSystem: RenderingSystem) -> String {
        switch renderingSystem {
            case .pycob:
                if type == .elements {
                    return "''' + '\\n'.join(map(lambda x: x.to_html(), self.components)) + ''' "
                }

                if type == .navbar {
                    return "''' + self.\(name).to_html() + '''"
                }

                if type == .footer {
                    return "''' + self.\(name).to_html() + '''"
                }

                if type == .optionalInt || type == .int {
                    return "''' + str(self.\(name)) + '''"
                }

                return "''' + self.\(name) + '''"

            case .react:
                return "{'\(name)}"
        }
    }

    func staticValue(val: String?) -> String {
        guard let val else {
            return defaultValue ?? ""
        }

        if val == "" {
            return defaultValue ?? ""
        }

        return val
    }
}

extension Array where Element == Argument {
    func templateVariables(in renderingSystem: RenderingSystem) -> String {
        return self.map { $0.templateVariable(in: renderingSystem) }.joined(separator: ", ")
    }

    func setDefaults() -> String {
        return self.compactMap {
            guard let defaultValue = $0.defaultValue else { return nil }
            return "'\($0.name)' : '\(defaultValue)'" 
        }.joined(separator: ", ")
    }

    func pythonArgumentListWithDefaults() -> String {
        if self.count == 0 {
            return "self"
        }

        return "self, " + self.map { 
            switch $0.type {
                case .int:
                    return "\($0.name): int"
                case .optionalInt:
                    return "\($0.name): int = \($0.defaultValue ?? "0")"
                case .string:
                    return "\($0.name): str"
                case .optionalString:
                    return "\($0.name): str = '\($0.defaultValue ?? "")'"
                case .optionalBool:
                    return "\($0.name): bool = \($0.defaultValue ?? "True")"
                case .bool:
                    return "\($0.name): bool"
                case .elements:
                    return "\($0.name): list = None"
                case .list:
                    return "\($0.name): list = []"
                case .navbar:
                    return "\($0.name): Navbar = \($0.defaultValue ?? "Navbar()")"
                case .footer:
                    return "\($0.name): Footer = \($0.defaultValue ?? "Footer()")"
                case .untyped:
                    return "\($0.name)"
            }
        }.joined(separator: ", ")
    }

    func pythonArgumentListNoTypes() -> String {
        return self.map { 
            $0.name
        }.joined(separator: ", ")
    }

    func pythonArgumentListSelfAssignment() -> String {
        if self.count == 0 {
            return "pass"
        }

        return self.map { 
            if $0.type == .elements {
                return "# https://stackoverflow.com/questions/4841782/python-constructor-and-default-value\n    self.\($0.name) = \($0.name) or []"
            } else {
                return "self.\($0.name) = \($0.name)"
            }
        }.joined(separator: "\n    ")
    }

    func pythonArgumentDocString() -> String {
        /*
            Args:
                param1 (int): The first parameter.
                param2 (str): The second parameter.
        */
        
        if self.count == 0 {
            return ""
        }

        return "Args:\n" + self.map { 
            switch $0.type {
                case .int:
                    return "        \($0.name) (int): \($0.description)"
                case .optionalInt:
                    return "        \($0.name) (int): Optional. \($0.description)"
                case .string:
                    return "        \($0.name) (str): \($0.description)"
                case .optionalString:
                    return "        \($0.name) (str): Optional. \($0.description)"
                case .optionalBool:
                    return "        \($0.name) (bool): Optional. \($0.description)"
                case .bool:
                    return "        \($0.name) (bool): \($0.description)"
                case .elements:
                    return "        \($0.name) (list): \($0.description)"
                case .list:
                    return "        \($0.name) (list): \($0.description)"
                case .navbar:
                    return "        \($0.name) (Navbar): \($0.description)"
                case .footer:
                    return "        \($0.name) (Footer): \($0.description)"
                case .untyped:
                    return "        \($0.name): \($0.description)"
            }
        }.joined(separator: "\n")
    }

    func staticValues(vals: [String]) -> String {
        return self.enumerated().map { $0.element.staticValue(val: vals[$0.offset]) }.joined(separator: ", ")
    }

    func get(_ name: String) -> Argument {
        return self.first { $0.name == name }!
    }
}

struct ExampleCode: Codable {
    let setup: [String]?
    let arguments: [ExampleArgument]
}

struct ExampleArgument: Codable {
    let argumentName: ArgumentName
    let argumentValue: ArgumentInstance
}

protocol Element: Encodable {
    var elementType: ElementType { get }
    var name: String { get }
    var attachableTo: [ElementType] { get }
    var category: DocumentationCategory { get }
    var description: String { get }
    var arguments: [Argument] { get }
    var postInitPythonFunc: String? { get }
    var exampleCode: [ExampleCode] { get }

    func toTailwindHtmlTemplate(in: RenderingSystem) -> String
}

struct PageElement: Element {
    let elementType: ElementType = .page
    let name: String = "Page"
    let attachableTo: [ElementType] = []
    let category: DocumentationCategory = .internal
    let description: String = "A page is the top level component of a website. It contains the navbar, the main content, and the footer."
    let arguments: [Argument] = [
        Argument(name: "title", type: .optionalString, description: "The SEO title of the page"),
        Argument(name: "description", type: .optionalString, description: "The SEO description of the page", defaultValue: ""),
        Argument(name: "image", type: .optionalString, description: "The SEO image of the page", defaultValue: ""),
        Argument(name: "additional_head", type: .optionalString, description: "Additional HTML to be added to the head of the page", defaultValue: ""),
        Argument(name: "navbar", type: .navbar, description: "Navbar for the page", defaultValue: "Navbar(title='PyVibe App')"),
        Argument(name: "footer", type: .footer, description: "Footer for the page", defaultValue: "Footer()"),
        Argument(name: "components", type: .elements, description: "The components to be rendered on the page"),
    ]
    let postInitPythonFunc: String? = nil
    let exampleCode: [ExampleCode] = [
        ExampleCode(setup: nil, arguments: 
        [
            ExampleArgument(argumentName: "title", argumentValue: .string("My Page"))
        ])
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let title: String = arguments.get("title").templateVariable(in: renderingSystem)
        let description: String = arguments.get("description").templateVariable(in: renderingSystem)
        let image: String = arguments.get("image").templateVariable(in: renderingSystem)
        let additional_head: String = arguments.get("additional_head").templateVariable(in: renderingSystem)
        let navbar: String = arguments.get("navbar").templateVariable(in: renderingSystem)
        let footer: String = arguments.get("footer").templateVariable(in: renderingSystem)
        let components: String = arguments.get("components").templateVariable(in: renderingSystem)

        return """
        <!doctype html>
            <html>
            <head>
            <meta charset="UTF-8">
            <link rel="apple-touch-icon" sizes="180x180" href="https://cdn.pycob.com/apple-touch-icon.png">
            <link rel="icon" type="image/png" sizes="32x32" href="https://cdn.pycob.com/favicon-32x32.png">
            <link rel="icon" type="image/png" sizes="16x16" href="https://cdn.pycob.com/favicon-16x16.png">
            <link rel="mask-icon" href="https://cdn.pycob.com/safari-pinned-tab.svg" color="#5bbad5">
            <link rel="shortcut icon" href="https://cdn.pycob.com/favicon.ico">
            <meta name="msapplication-TileColor" content="#603cba">
            <meta name="msapplication-config" content="https://cdn.pycob.com/browserconfig.xml">
            <meta name="theme-color" content="#ffffff">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>\(title)</title>
            <meta property="og:title" content="\(title)">
            <meta property="og:description" content="\(description)">
            <meta property="og:image" content="\(image)">
            \(additional_head)
            <script src="https://cdn.tailwindcss.com"></script>
            <script src="https://unpkg.com/ag-grid-community/dist/ag-grid-community.min.js"></script>
            <script src="https://cdn.plot.ly/plotly-2.18.2.min.js"></script>
            <script>
                tailwind.config = {
                    theme: {
                        extend: {
                            colors: {
                                clifford: '#da373d',
                            }
                        }
                    },
                    darkMode: 'class'
                }
            </script>
            <script>
            function toggleDarkMode() {
                if (document.documentElement.classList.contains('dark')) {
                    document.documentElement.classList.remove('dark')
                    document.getElementById("moon").classList.add("hidden")
                    document.getElementById("sun").classList.remove("hidden")
                } else {
                    document.documentElement.classList.add('dark')
                    document.getElementById("sun").classList.add("hidden")
                    document.getElementById("moon").classList.remove("hidden")
                }
            }

            function setLoading(el) {
                el.querySelectorAll("button[type=submit]").forEach((button) => {
                    button.innerHTML = '<svg aria-hidden="true" role="status" class="inline w-4 h-4 mr-3 text-white animate-spin" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="#E5E7EB"/><path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentColor"/></svg>Loading...';
                    button.disabled = true;
                });
            }

            function toggleMore(button) {
                x = button

                if (x.innerHTML === "more") {
                    x.innerHTML = "less";
                    text_full = x.getAttribute("data-text-full")
                    text_truncated = x.getAttribute("data-text-truncated")

                    x.parentElement.innerHTML = text_full + ' <button data-text-full="' + text_full + '" data-text-truncated="' + text_truncated + '" onclick="toggleMore(this)" class="text-blue-500">less</button>'
                } else {
                    x.innerHTML = "more";
                    text_full = x.getAttribute("data-text-full")
                    text_truncated = x.getAttribute("data-text-truncated")

                    x.parentElement.innerHTML = text_truncated + ' <button data-text-full="' + text_full + '" data-text-truncated="' + text_truncated + '" onclick="toggleMore(this)" class="text-blue-500">more</button>'
                }
            }
            </script>
            <style>
            .gradient-background {
                background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
                background-size: 400% 400%;
                animation: gradient 180s ease infinite;
            }

            .gradient-text {
                color: transparent;
                background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
                background-clip: text;
                -webkit-background-clip: text;
                animation: gradient 2s ease infinite;
            }

            @keyframes gradient {
                0% {
                    background-position: 0% 50%;
                }
                50% {
                    background-position: 100% 50%;
                }
                100% {
                    background-position: 0% 50%;
                }
            }
            </style>
            </head>
            <body class="flex flex-col h-screen dark:bg-gray-900 ">
                \(navbar)
                <div id="page-container" class="container px-5 my-5 mx-auto">
                    \(components)
                </div>
                \(footer)
            </body>
        </html>
        """
    }
}

struct HtmlElement: Element {
    let elementType: ElementType = .html
    let name: String = "HTML"
    let attachableTo: [ElementType] = [.page, .card, .container]
    let category: DocumentationCategory = .basicHtml
    let description: String = "Renders raw HTML. This is meant to be an escape hatch for when you need to render something that isn't supported by PyVibe."
    let arguments: [Argument] = [Argument(name: "value", type: .string, description: "Raw HTML code to be rendered")]
    let postInitPythonFunc: String? = nil
    let exampleCode: [ExampleCode] = [
        ExampleCode(setup: nil, arguments: 
        [
            ExampleArgument(argumentName: "value", argumentValue: .string("<b>here's some html</b>"))
        ]
        )
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let value = arguments.get("value")
        return "\(value.templateVariable(in: renderingSystem))"
    }
}

struct TextElement: Element {
    let elementType: ElementType = .text
    let name: String = "Text"
    let attachableTo: [ElementType] = [.page, .card, .container, .form]
    let category: DocumentationCategory = .basicHtml
    let description: String = "Renders a paragraph of text"
    let arguments: [Argument] = [Argument(name: "value", type: .string, description: "Text to be rendered")]
    let postInitPythonFunc: String? = nil
    let exampleCode: [ExampleCode] = [
        ExampleCode(setup: nil, arguments: [
            ExampleArgument(argumentName: "value", argumentValue: .string("Here's some text"))
        ])
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let value = arguments.get("value").templateVariable(in: renderingSystem)
        
        return """
        <p class="mb-6 text-lg font-normal text-gray-500 lg:text-xl dark:text-gray-400">\(value)</p>
        """
    }
}

struct PlainLinkElement: Element {
    let elementType: ElementType = .plainlink
    let name: String = "Unstyled Link"
    let attachableTo: [ElementType] = [.page, .navbar, .card, .container]
    let category: DocumentationCategory = .basicHtml
    let description: String = "Renders a link without any styling"
    let arguments: [Argument] = 
            [ Argument(name: "text", type: .string, description: "Text to be rendered"),
              Argument(name: "url", type: .string, description: "URL to link to"),
              Argument(name: "classes", type: .optionalString, description: "Classes to be applied to the link", defaultValue: "")
            ]
    let postInitPythonFunc: String? = nil
    let exampleCode: [ExampleCode] = [
        ExampleCode(setup: nil, arguments: [ 
            ExampleArgument(argumentName: "text", argumentValue: .string("Here's a link")),
            ExampleArgument(argumentName: "url", argumentValue: .string("https://www.pycob.com"))
        ])
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let text = arguments.get("text")
        let url = arguments.get("url")
        let classes = arguments.get("classes").templateVariable(in: renderingSystem)

        return "<a class=\"\(classes)\" href=\"\(url.templateVariable(in: renderingSystem))\">\(text.templateVariable(in: renderingSystem))</a>"
    }
}

struct ListElement: Element {
    let elementType: ElementType = .list
    let name: String = "List"
    let attachableTo: [ElementType] = [.page, .card, .container, .form]
    let category: DocumentationCategory = .basicHtml
    let description: String = "Renders a list of items"
    let arguments: [Argument] = [
        Argument(name: "show_dots", type: .optionalBool, description: "Whether or not to show dots", defaultValue: "True"),
        Argument(name: "classes", type: .optionalString, description: "Classes to be applied to the list", defaultValue: ""),
        Argument(name: "components", type: .elements, description: "Items to be rendered")
    ]
    let postInitPythonFunc: String? = """
    if self.show_dots:
        self.classes += "list-disc"
    else:
        self.classes += "list-none"
    """
    let exampleCode: [ExampleCode] = [
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let components = arguments.get("components").templateVariable(in: renderingSystem)
        let classes = arguments.get("classes").templateVariable(in: renderingSystem)

        return """
        <ul class="max-w-md space-y-1 text-gray-500 list-inside dark:text-gray-400 \(classes)">
            \(components)
        </ul>
        """
    }
}

struct ListItemElement: Element {
    let elementType: ElementType = .listitem
    let name: String = "List Item"
    let attachableTo: [ElementType] = [.list]
    let category: DocumentationCategory = .basicHtml
    let description: String = "Renders an item in a list"
    let arguments: [Argument] = [
        Argument(name: "value", type: .string, description: "Text to be rendered"),
        Argument(name: "classes", type: .optionalString, description: "Classes to be applied to the list item", defaultValue: ""),
        Argument(name: "svg", type: .optionalString, description: "SVG to render inside the list", defaultValue: ""),
        Argument(name: "is_checked", type: .optionalBool, description: "Whether or not the item is checked", defaultValue: "None")
    ]
    let postInitPythonFunc: String? = """
    if self.is_checked is not None:
        if self.is_checked:
            self.svg = '''<svg class="w-4 h-4 mr-1.5 text-green-500 dark:text-green-400 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path></svg>'''
        else:
            self.svg = '''<svg class="w-4 h-4 mr-1.5 text-gray-400 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd"></path></svg>'''
    """
    let exampleCode: [ExampleCode] = [
        ExampleCode(setup: nil, arguments: [
            ExampleArgument(argumentName: "value", argumentValue: .string("Item 1"))
        ])
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let value = arguments.get("value").templateVariable(in: renderingSystem)
        let svg = arguments.get("svg").templateVariable(in: renderingSystem)
        let classes = arguments.get("classes").templateVariable(in: renderingSystem)

        return """
        <li class="flex items-center \(classes)">
            \(svg)
            \(value)
        </li>
        """
    }
}

struct LinkElement: Element {
    let elementType: ElementType = .link
    let name: String = "Link"
    let attachableTo: [ElementType] = [.page, .navbar, .card, .form, .container]
    let category: DocumentationCategory = .basicHtml
    let description: String = "Renders a link"
    let arguments: [Argument] = 
            [ Argument(name: "text", type: .string, description: "Text to be rendered"),
              Argument(name: "url", type: .string, description: "URL to link to"),
              Argument(name: "classes", type: .optionalString, description: "Classes to be applied to the link", defaultValue: "")
            ]
    let postInitPythonFunc: String? = nil
    let exampleCode: [ExampleCode] = [
        ExampleCode(setup: nil, arguments: [ 
            ExampleArgument(argumentName: "text", argumentValue: .string("Here's a link")),
            ExampleArgument(argumentName: "url", argumentValue: .string("https://www.pycob.com"))
        ])
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let text = arguments.get("text").templateVariable(in: renderingSystem)
        let url = arguments.get("url").templateVariable(in: renderingSystem)
        let classes = arguments.get("classes").templateVariable(in: renderingSystem)

        return """
        <p class="text-gray-500 dark:text-gray-400 \(classes)">
            <a href="\(url)" class="inline-flex items-center font-medium text-blue-600 dark:text-blue-500 hover:underline">
            \(text)
            <svg aria-hidden="true" class="w-5 h-5 ml-1" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
            </a>
        </p>
        """
    }
}

struct ImageElement: Element {
    let elementType: ElementType = .image
    let name: String = "Image"
    let attachableTo: [ElementType] = [.page, .card, .form, .container]
    let category: DocumentationCategory = .basicHtml
    let description: String = "Renders an image"
    let arguments: [Argument] = 
            [ Argument(name: "url", type: .string, description: "URL of the image"),
              Argument(name: "alt", type: .string, description: "Alt text for the image", defaultValue: "Image"),
              Argument(name: "classes", type: .optionalString, description: "Classes to be applied to the image", defaultValue: ""),
            ]
    let postInitPythonFunc: String? = nil
    let exampleCode: [ExampleCode] = [
        ExampleCode(setup: nil, arguments: [ 
            ExampleArgument(argumentName: "url", argumentValue: .string("https://cdn.pycob.com/pycob_with_text_256.png")),
            ExampleArgument(argumentName: "alt", argumentValue: .string("Pycob logo"))
        ])
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let url = arguments.get("url").templateVariable(in: renderingSystem)
        let alt = arguments.get("alt").templateVariable(in: renderingSystem)
        let classes = arguments.get("classes").templateVariable(in: renderingSystem)

        return "<img class=\"max-w-fit h-auto rounded-lg \(classes) \" src=\"\(url)\" alt=\"\(alt)\">"
    }
}

struct HeaderElement: Element {
    let elementType: ElementType = .header
    let name: String = "Header"
    let attachableTo: [ElementType] = [.page, .card, .container]
    let category: DocumentationCategory = .basicHtml
    let description: String = "Renders a header"
    let arguments: [Argument] = 
            [ Argument(name: "text", type: .string, description: "Text to be rendered"),
              Argument(name: "size", type: .optionalInt, description: "Size of the header. Choose 1-9", defaultValue: "5"),
              Argument(name: "classes", type: .optionalString, description: "Classes to be applied to the header", defaultValue: "")
            ]
    let postInitPythonFunc: String? = """
    if size == 1:
        self.classes += " text-lg sm:text-xl"
    elif size == 2:
        self.classes += " text-lg sm:text-2xl"
    elif size == 3:
        self.classes += " text-lg sm:text-3xl"
    elif size == 4:
        self.classes += " text-lg sm:text-4xl"
    elif size == 5:
        self.classes += " text-xl sm:text-5xl"
    elif size == 6:
        self.classes += " text-2xl sm:text-6xl"
    elif size == 7:
        self.classes += " text-3xl sm:text-7xl"
    elif size == 8:
        self.classes += " text-4xl sm:text-8xl"
    elif size == 9:
        self.classes += " text-5xl sm:text-9xl"
    else:
        raise ValueError("Header size must be between 1 and 9")
    """
    let exampleCode: [ExampleCode] = [
        ExampleCode(setup: nil, arguments: [ 
            ExampleArgument(argumentName: "text", argumentValue: .string("Here's a regular header"))
        ]),
        ExampleCode(setup: nil, arguments: [ 
            ExampleArgument(argumentName: "text", argumentValue: .string("Here's a small header")),
            ExampleArgument(argumentName: "size", argumentValue: .int(1))
        ]),
        ExampleCode(setup: nil, arguments: [ 
            ExampleArgument(argumentName: "text", argumentValue: .string("Here's a big header")),
            ExampleArgument(argumentName: "size", argumentValue: .int(8))
        ])
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let text = arguments.get("text").templateVariable(in: renderingSystem)
        let classes = arguments.get("classes").templateVariable(in: renderingSystem)
        
        return """
        <p class="mb-4 font-extrabold leading-none tracking-tight text-gray-900 dark:text-white \(classes) ">\(text)</p>
        """
    }
}

// Layout Elements

struct CardElement: Element {
    let elementType: ElementType = .card
    let name: String = "Card"
    let attachableTo: [ElementType] = [.page, .card, .container]
    let category: DocumentationCategory = .layout
    let description: String = "Renders a card"
    let arguments: [Argument] = 
            [ Argument(name: "center_content", type: .optionalBool, description: "Whether the card contents should be centered", defaultValue: "False"),
              Argument(name: "classes", type: .optionalString, description: "Classes to be applied to the card", defaultValue: ""),
              Argument(name: "components", type: .elements, description: "Components to be rendered inside the card"),
            ]
    let postInitPythonFunc: String? = nil    
    let exampleCode: [ExampleCode] = [
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let components = arguments.get("components").templateVariable(in: renderingSystem)
        let classes = arguments.get("classes").templateVariable(in: renderingSystem)

        return """
        <div class="block p-6 mb-6 bg-white border border-gray-200 rounded-lg shadow-md hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700 overflow-x-auto max-w-fit mx-auto \(classes)">
            <div class="flex flex-col h-full ">
                \(components)
            </div>
        </div>
        """
    }
}

struct ContainerElement: Element {
    let elementType: ElementType = .container
    let name: String = "Container"
    let attachableTo: [ElementType] = [.page, .card, .container, .form]
    let category: DocumentationCategory = .layout
    let description: String = "Renders a container to help with layout"
    let arguments: [Argument] = 
            [ Argument(name: "grid_columns", type: .optionalInt, description: "Number of columns (if any) to use. 1-12", defaultValue: "None"),
              Argument(name: "classes", type: .optionalString, description: "Classes to be applied to the container", defaultValue: ""),
              Argument(name: "components", type: .elements, description: "Components to be rendered inside the container"),
            ]
    let postInitPythonFunc: String? = """
    if grid_columns is not None:
        self.classes += " grid gap-6 md:grid-cols-" + str(grid_columns)
    """    
    let exampleCode: [ExampleCode] = [
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let components = arguments.get("components").templateVariable(in: renderingSystem)
        let classes = arguments.get("classes").templateVariable(in: renderingSystem)

        return """
        <div class=" \(classes)">
            \(components)
        </div>
        """
    }
}

struct AlertElement: Element {
    let elementType: ElementType = .alert
    let name: String = "Alert"
    let attachableTo: [ElementType] = [.page, .card, .container]
    let category: DocumentationCategory = .layout
    let description: String = "Renders an alert"
    let arguments: [Argument] = 
            [ Argument(name: "text", type: .string, description: "Text to be rendered"),
              Argument(name: "badge", type: .optionalString, description: "Text to be rendered inside the badge"),
              Argument(name: "color", type: .optionalString, description: "Color of the. Choose 'indigo', 'orange', or 'red'", defaultValue: "indigo")
            ]
    let postInitPythonFunc: String? = nil
    let exampleCode: [ExampleCode] = [
        ExampleCode(setup: nil, arguments: [ 
            ExampleArgument(argumentName: "text", argumentValue: .string("Here's a success alert"))
        ]),
        ExampleCode(setup: nil, arguments: [ 
            ExampleArgument(argumentName: "text", argumentValue: .string("Here's a warning alert")),
            ExampleArgument(argumentName: "badge", argumentValue: .string("Warning")),
            ExampleArgument(argumentName: "color", argumentValue: .string("orange"))
        ]),
        ExampleCode(setup: nil, arguments: [ 
            ExampleArgument(argumentName: "text", argumentValue: .string("Here's an error alert")),
            ExampleArgument(argumentName: "badge", argumentValue: .string("Delete?")),
            ExampleArgument(argumentName: "color", argumentValue: .string("red"))
        ])
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let text = arguments.get("text")
        let badge = arguments.get("badge")
        let color = arguments.get("color")
        
        return """
        <div class="text-center py-4 lg:px-4">
        <div class="p-2 bg-\(color.templateVariable(in: renderingSystem))-800 items-center text-\(color.templateVariable(in: renderingSystem))-100 leading-none lg:rounded-full flex lg:inline-flex" role="alert">
            <span class="flex rounded-full bg-\(color.templateVariable(in: renderingSystem))-500 uppercase px-2 py-1 text-xs font-bold mr-3">\(badge.templateVariable(in: renderingSystem))</span>
            <span class="font-semibold mr-2 text-left flex-auto">\(text.templateVariable(in: renderingSystem))</span>            
        </div>
        </div>
        """
    }
}

struct CodeElement: Element {
    let elementType: ElementType = .code
    let name: String = "Code"
    let attachableTo: [ElementType] = [.page, .form, .card, .container]
    let category: DocumentationCategory = .basicHtml
    let description: String = "Renders a block of code"
    let arguments: [Argument] = [
        Argument(name: "value", type: .string, description: "Code to be rendered"), 
        Argument(name: "header", type: .optionalString, description: "Header to be rendered above the code block"),
        Argument(name: "prefix", type: .optionalString, description: "Prefix to be rendered before the code block", defaultValue: ">>>"),
    ]
    let postInitPythonFunc: String? = """
    # Replace < and > in prefix:
    self.prefix = self.prefix.replace("<", "&lt;").replace(">", "&gt;")
    """
    let exampleCode: [ExampleCode] = [
        ExampleCode(setup: nil, arguments: [ExampleArgument(argumentName: "value", argumentValue: .string("Here's some code"))]),
        ExampleCode(setup: nil, arguments: [ExampleArgument(argumentName: "value", argumentValue: .string("Here's some code with a header")), ExampleArgument(argumentName: "header", argumentValue: .string("With Header"))])
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let value = arguments.get("value").templateVariable(in: renderingSystem)
        let header = arguments.get("header").templateVariable(in: renderingSystem)
        let prefixText = arguments.get("prefix").templateVariable(in: renderingSystem)

        return """
        <div class="mx-auto my-10 max-w-3xl">
            <div class="flex h-11 w-full items-center justify-start space-x-1.5 rounded-t-lg bg-gray-900 px-3">
                <span class="h-3 w-3 rounded-full bg-red-400"></span>
                <span class="h-3 w-3 rounded-full bg-yellow-400"></span>
                <span class="h-3 w-3 rounded-full bg-green-400"></span>
                <code class="pl-5 text-lime-500">\(header)</code>
            </div>
            <div class="w-full border-t-0 bg-gray-700 pb-5 rounded-b-lg whitespace-nowrap overflow-x-scroll p-2">
                <code class="text-gray-500">\(prefixText)</code>
                <code class="text-white" style="white-space: break-spaces">\(value)</code>
            </div>
        </div>
        """
    }
}

struct CodeEditorElement: Element {
    let elementType: ElementType = .codeeditor
    let name: String = "Code Editor"
    let attachableTo: [ElementType] = [.page]
    let category: DocumentationCategory = .internal
    let description: String = "Renders a code editor"
    let arguments: [Argument] = [
        Argument(name: "value", type: .string, description: "Code to be rendered"),
        Argument(name: "language", type: .optionalString, description: "Language mode for syntax highlighting", defaultValue: "python"),
    ]
    let postInitPythonFunc: String? = nil
    let exampleCode: [ExampleCode] = [
        ExampleCode(setup: nil, arguments: [ExampleArgument(argumentName: "value", argumentValue: .string("Here's some code"))]),
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let value = arguments.get("value").templateVariable(in: renderingSystem)
        let language = arguments.get("language").templateVariable(in: renderingSystem)

        return """
<style type="text/css" media="screen">
#editorContainer {
    // width: calc( 100vw - 40px );
    height: 500px;
    max-height: calc( 80vh - 60px );
    position: relative;
    background-color: red;
}
#editor { 
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
}
</style>

<div id="editorContainer">
    <div id="editor">\(value)</div> 
</div>
<script src="https://cdn.jsdelivr.net/gh/ajaxorg/ace-builds/src-noconflict/ace.js" type="text/javascript" charset="utf-8"></script>
<script>
    var editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
    editor.session.setMode("ace/mode/\(language)");

    // const savedCode = localStorage.getItem('code');

    // if (savedCode) {
    //     editor.setValue(savedCode);
    // }
</script>
"""
    }
}

struct EmGithubElement: Element {
    let elementType: ElementType = .emgithub
    let name: String = "Github Embed"
    let attachableTo: [ElementType] = [.page, .card]
    let category: DocumentationCategory = .advanced
    let description: String = "Renders a block of code from a github URL"
    let arguments: [Argument] = [Argument(name: "url", type: .string, description: "URL of the GitHub file to be rendered")]
    let postInitPythonFunc: String? = nil
    let exampleCode: [ExampleCode] = [        
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        return " Advanced Component "
    }        
}

struct DividerElement: Element {
    let elementType: ElementType = .divider
    let name: String = "Divider"
    let attachableTo: [ElementType] = [.page, .card]
    let category: DocumentationCategory = .basicHtml
    let description: String = "Renders a divider"
    let arguments: [Argument] = []
    let postInitPythonFunc: String? = nil
    let exampleCode: [ExampleCode] = [
        ExampleCode(setup: nil, arguments: [])
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        return """
        <hr class="my-5 border-gray-300 w-full">
        """
    }
}

struct SectionElement: Element {
    let elementType: ElementType = .section
    let name: String = "Section"
    let attachableTo: [ElementType] = [.page]
    let category: DocumentationCategory = .layout
    let description: String = "Creates an invisible element that can be used to link to in the sidebar"
    let arguments: [Argument] = [
        Argument(name: "id", type: .string, description: "ID for the section. This is what will appear in the link as /page#id"), 
        Argument(name: "name", type: .string, description: "Name of the section. This is what will appear in the navigation bar"), 
        Argument(name: "level", type: .optionalInt, description: "Level of the section. This is the indentation that will appear in the navigation bar", defaultValue: "1")
    ]
    let postInitPythonFunc: String? = nil
    let exampleCode: [ExampleCode] = [
        ExampleCode(setup: nil, arguments: [ExampleArgument(argumentName: "id", argumentValue: .string("section1")), ExampleArgument(argumentName: "name", argumentValue: .string("Sample Section 1"))]),
        ExampleCode(setup: nil, arguments: [ExampleArgument(argumentName: "id", argumentValue: .string("section2")), ExampleArgument(argumentName: "name", argumentValue: .string("Sample Section 2")), ExampleArgument(argumentName: "level", argumentValue: .int(2))])  
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let id = arguments.get("id")

        return """
        <span id=\(id.templateVariable(in: renderingSystem))></span>
        """
    }

    func toTailwindSidebarHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let id = arguments.get("id")
        let name = arguments.get("name")
        let level = arguments.get("level")
/*
                    <a href="#" class="flex items-center space-x-1 rounded-md px-2 py-3 hover:bg-gray-100 hover:text-blue-600">
                        <span class="text-2xl"><i class="bx bx-home"></i></span>
                        <span>Anchor 1</span>
                    </a>
*/
// <a href="#item-1" class="hs-scrollspy-active:text-blue-600 dark:hs-scrollspy-active:text-blue-400 active block py-0.5 text-sm font-medium leading-6 text-slate-700 hover:text-slate-900 dark:text-slate-400 dark:hover:text-slate-300">Item 1</a>
//                 
        return """
        <a href="#\(id.templateVariable(in: renderingSystem))" class="ml-\(level.templateVariable(in: renderingSystem)) flex items-center space-x-1 rounded-md px-2 py-3 hover:bg-gray-100 hover:text-blue-600">
            <span class="text-2xl"><i class="bx bx-home"></i></span>
            <span>\(name.templateVariable(in: renderingSystem))</span>
        </a>
        """
    }
}

struct NavbarElement: Element {
    let elementType: ElementType = .navbar
    let name: String = "Navbar"
    let attachableTo: [ElementType] = []
    let category: DocumentationCategory = .internal
    let description: String = "Renders a navbar"
    let postInitPythonFunc: String? = """
    if button_label == "Sign In" and button_svg == "":
        self.button_svg = '<svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="ml-1 h-4 w-4" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"></path></svg>'

    if button_svg == "":
        self.button_svg = '<svg fill="none" stroke="currentColor" stroke-width="1.5" class="ml-1 h-4 w-4" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z"></path></svg>'
    """
    let arguments: [Argument] = [
        Argument(name: "title", type: .string, description: "Title of the navbar"),        
        Argument(name: "logo", type: .optionalString, description: "URL for the logo of the navbar", defaultValue: "https://cdn.pycob.com/pycob_hex.png"),
        Argument(name: "button_label", type: .optionalString, description: "Label for the button", defaultValue: "Sign In"),
        Argument(name: "button_url", type: .optionalString, description: "URL for the button", defaultValue: "/auth/login"),
        Argument(name: "button_svg", type: .optionalString, description: "SVG for the button", defaultValue: ""),
        Argument(name: "components", type: .elements, description: "List of links for the navbar")
    ]

    let exampleCode: [ExampleCode] = [
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let logo = arguments.get("logo").templateVariable(in: renderingSystem)
        let title = arguments.get("title").templateVariable(in: renderingSystem)
        let components = arguments.get("components").templateVariable(in: renderingSystem)
        let button_label = arguments.get("button_label").templateVariable(in: renderingSystem)
        let button_url = arguments.get("button_url").templateVariable(in: renderingSystem)
        let button_svg = arguments.get("button_svg").templateVariable(in: renderingSystem)

        return """
<script>
    function toggleNav() {
        var nav = document.getElementById("navbar-sticky");
        if (nav.classList.contains("hidden")) {
            nav.classList.remove("hidden");
        } else {
            nav.classList.add("hidden");
        }
    }
</script>
<nav class="gradient-background top-0 left-0 z-20 w-full bg-white px-2 py-2.5 dark:border-gray-600 sm:px-4">
    <div class="container mx-auto flex flex-wrap items-center justify-between">
      <a href="/" class="flex items-center">
        <img src="\(logo)" class="mr-3 h-6 sm:h-9" style="filter: brightness(0) invert(1);" alt="Logo" />
        <span class="self-center whitespace-nowrap md:text-4xl font-semibold text-white">\(title)</span>
      </a>
      <div class="flex md:order-2">
        <button onclick="toggleDarkMode()" type="button" class="mx-3 px-3 py-2 text-xs font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 bg-gradient-to-br from-purple-600 to-blue-500 group-hover:from-purple-600 group-hover:to-blue-500">
            <svg id="sun" data-toggle-icon="sun" class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" fill-rule="evenodd" clip-rule="evenodd"></path></svg>
            <svg id="moon" data-toggle-icon="moon" class="w-4 h-4 hidden" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"></path></svg>        </button>
        <a type="button" href="\(button_url)" id="pycob-login-button" class="mr-3 inline-flex items-center rounded-lg bg-blue-700 px-2 py-1 text-center text-xs font-medium text-white hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 md:mr-0">
          \(button_label)
          \(button_svg)
        </a>
        <button onclick="toggleNav()" data-collapse-toggle="navbar-sticky" type="button" class="inline-flex items-center rounded-lg p-2 text-sm text-white hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-white dark:hover:bg-gray-700 dark:focus:ring-gray-600 md:hidden" aria-controls="navbar-sticky" aria-expanded="true">
          <span class="sr-only">Open main menu</span>
          <svg class="h-6 w-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clip-rule="evenodd"></path></svg>
        </button>
      </div>
      <div class="w-full items-center justify-between md:order-1 md:flex md:w-auto hidden" id="navbar-sticky">
        <ul class="mt-4 flex flex-col rounded-lg md:mt-0 md:flex-row md:space-x-8 md:border-0 md:text-sm md:font-medium">
          \(components)
        </ul>
      </div>
    </div>
  </nav>
"""
    }
}

struct NavbarLinkElement: Element {
    let elementType: ElementType = .navbarlink
    let name: String = "Navbar Link"
    let attachableTo: [ElementType] = [.navbar]
    let category: DocumentationCategory = .internal
    let description: String = "Renders a link in the navbar"
    let arguments: [Argument] = 
            [ Argument(name: "text", type: .string, description: "Text to be rendered"),
              Argument(name: "url", type: .string, description: "URL to link to"),
              Argument(name: "classes", type: .optionalString, description: "Classes to be applied to the link", defaultValue: "")
            ]
    let postInitPythonFunc: String? = nil
    let exampleCode: [ExampleCode] = []

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let text: String = arguments.get("text").templateVariable(in: renderingSystem)
        let url: String = arguments.get("url").templateVariable(in: renderingSystem)
        let classes: String = arguments.get("classes").templateVariable(in: renderingSystem)

        return "<a class=\"block rounded-lg py-2 pl-3 pr-4 text-white hover:bg-blue-800 md:p-2 \(classes)\" href=\"\(url)\">\(text)</a>"
    }
}

struct FooterElement: Element {
    let elementType: ElementType = .footer
    let name: String = "Footer"
    let attachableTo: [ElementType] = []
    let category: DocumentationCategory = .internal
    let description: String = "Renders a footer"
    let postInitPythonFunc: String? = nil
    let arguments: [Argument] = [
        Argument(name: "title", type: .optionalString, description: "Title of the footer", defaultValue: ""),
        Argument(name: "subtitle", type: .optionalString, description: "Subtitle of the footer", defaultValue: ""),
        Argument(name: "logo", type: .optionalString, description: "URL for the logo of the footer", defaultValue: ""),
        Argument(name: "components", type: .elements, description: "List of category components for the footer")
    ]

    let exampleCode: [ExampleCode] = [
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let title = arguments.get("title").templateVariable(in: renderingSystem)
        let subtitle = arguments.get("subtitle").templateVariable(in: renderingSystem)
        let logo = arguments.get("logo").templateVariable(in: renderingSystem)
        let components = arguments.get("components").templateVariable(in: renderingSystem)

        return """
        <footer class="text-gray-600 body-font">
            <div class="container px-5 mx-auto flex md:items-center lg:items-start md:flex-row md:flex-nowrap flex-wrap flex-col">
                <div class="w-64 flex-shrink-0 md:mx-0 mx-auto text-center md:text-left">
                    <a class="flex title-font font-medium items-center md:justify-start justify-center text-gray-900 dark:text-white"><img class="object-scale-down h-10" src="\(logo)"><span class="ml-3 text-xl">\(title)</span></a>
                    <p class="mt-2 text-sm text-gray-500">\(subtitle)</p>
                </div>
                <div class="flex-grow flex flex-wrap md:pl-20 -mb-10 md:mt-0 mt-10 md:text-left text-center">
                    \(components)
                </div>
            </div>
        </footer>
        """
    }
}

struct FooterCategoryElement: Element {
    let elementType: ElementType = .footercategory
    let name: String = "Footer Category"
    let attachableTo: [ElementType] = [.footer]
    let category: DocumentationCategory = .internal
    let description: String = "Renders a category in the footer"
    let postInitPythonFunc: String? = nil
    let arguments: [Argument] = [
        Argument(name: "title", type: .string, description: "Title of the category"),
        Argument(name: "components", type: .elements, description: "List of Footer Link in the category"),
    ]
    let exampleCode: [ExampleCode] = [
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let title = arguments.get("title").templateVariable(in: renderingSystem)
        let components = arguments.get("components").templateVariable(in: renderingSystem)

        return """
        <div class="lg:w-1/4 md:w-1/2 w-full px-4">
            <h2 class="title-font font-medium text-gray-900 dark:text-white tracking-widest text-sm mb-3 uppercase">\(title)</h2>
            <nav class="list-none mb-10">
                \(components)
            </nav>
        </div>
        """
    }
}

struct FooterLinkElement: Element {
    let elementType: ElementType = .footerlink
    let name: String = "Footer Link"
    let attachableTo: [ElementType] = [.footercategory]
    let category: DocumentationCategory = .internal
    let description: String = "Renders a link in the footer"
    let postInitPythonFunc: String? = nil
    let arguments: [Argument] = [
        Argument(name: "title", type: .string, description: "Title of the link"),
        Argument(name: "url", type: .string, description: "URL of the link"),
    ]
    let exampleCode: [ExampleCode] = [
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let title = arguments.get("title").templateVariable(in: renderingSystem)
        let url = arguments.get("url").templateVariable(in: renderingSystem)

        return """
        <li><a href="\(url)" class="text-gray-600 hover:text-gray-800 dark:hover:text-white">\(title)</a></li>
        """
    }
}

struct FormElement: Element {
    let elementType: ElementType = .form
    let name: String = "Form"
    let attachableTo: [ElementType] = [.page, .card, .container]
    let category: DocumentationCategory = .form
    let description: String = "Renders a form"
    let postInitPythonFunc: String? = nil
    let arguments: [Argument] = [
        Argument(name: "action", type: .optionalString, description: "Action for the form. This is the page that the form will submit to. Defaults to the current page", defaultValue: "?"),
        Argument(name: "method", type: .optionalString, description: "Method for the form (i.e. GET, POST)", defaultValue: "GET"),
        Argument(name: "components", type: .elements, description: "List of Component of the form"),        
    ]
    let exampleCode: [ExampleCode] = [

    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let action = arguments.get("action")
        let method = arguments.get("method")
        let components = arguments.get("components").templateVariable(in: renderingSystem)

        return """
        <form class="max-w-full" style="width: 500px" onsubmit="setLoading(this)" action="\(action.templateVariable(in: renderingSystem))" method="\(method.templateVariable(in: renderingSystem))">
            \(components)
        </form>
        """
    }
}

struct SidebarElement: Element {
    let elementType: ElementType = .sidebar
    let name: String = "Sidebar"
    let attachableTo: [ElementType] = []
    let category: DocumentationCategory = .internal
    let description: String = "Renders a sidebar"
    let postInitPythonFunc: String? = nil
    let arguments: [Argument] = [
        Argument(name: "components", type: .elements, description: "List of Component of the sidebar"),
    ]
    let exampleCode: [ExampleCode] = [
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let components = arguments.get("components").templateVariable(in: renderingSystem)

        return """
        <style>
        @media (min-width: 1024px) {
            #page-container {
                max-width: calc( 100vw - 320px );
            }
        }
        </style>
        <script>
            function smoothScrollTo(link) {
                console.log(link);
                var hashUrl = link.href;
                console.log(hashUrl);
                var hash = hashUrl.substring(hashUrl.indexOf("#") + 1);
                console.log(hash);
                var element = document.getElementById(hash);
                console.log(element);
                if (element) {
                    element.scrollIntoView({behavior: "smooth", block: "start", inline: "nearest"})
                }
                return true;
            }
        </script>
        <aside style="min-width: 300px" class="hidden lg:block overflow-y-auto flex w-72 flex-col space-y-2 bg-gray-50 dark:bg-gray-800 p-2 h-screen sticky top-0">
            <div class="sticky top-0">
                \(components)
            </div>
        </aside>
        """
    }
}

struct SidebarCategoryElement: Element {
    let elementType: ElementType = .sidebarcategory
    let name: String = "Sidebar Category"
    let attachableTo: [ElementType] = [.sidebar]
    let category: DocumentationCategory = .internal
    let description: String = "Renders a category in the sidebar"
    let arguments: [Argument] = [
        Argument(name: "title", type: .string, description: "Title of the category"),
        Argument(name: "components", type: .elements, description: "List of Sidebar Link in the category"),
    ]
    let postInitPythonFunc: String? = nil
    let exampleCode: [ExampleCode] = [
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let title = arguments.get("title").templateVariable(in: renderingSystem)
        let components = arguments.get("components").templateVariable(in: renderingSystem)

        return """
        <div class="mb-8">
            <h2 class="text-lg font-medium text-gray-500 dark:text-gray-400 tracking-wider uppercase mb-3">\(title)</h2>
            <ul class="ml-5 list-none">
                \(components)
            </ul>
        </div>
        """
    }
}

struct SidebarLinkElement: Element {
    let elementType: ElementType = .sidebarlink
    let name: String = "Sidebar Link"
    let attachableTo: [ElementType] = [.sidebarcategory]
    let category: DocumentationCategory = .internal
    let description: String = "Renders a link in the sidebar"
    let arguments: [Argument] = [
        Argument(name: "title", type: .string, description: "Title of the link"),
        Argument(name: "url", type: .string, description: "URL of the link"),
    ]
    let postInitPythonFunc: String? = nil
    let exampleCode: [ExampleCode] = [
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let title = arguments.get("title").templateVariable(in: renderingSystem)
        let url = arguments.get("url").templateVariable(in: renderingSystem)

        return """
        <li><a href="\(url)" onclick="event.preventDefault(); smoothScrollTo(this)" class="text-gray-900 dark:text-white hover:text-gray-800">\(title)</a></li>
        """
    }
}

struct FormTextElement: Element {
    let elementType: ElementType = .formtext
    let name: String = "Form Text"
    let attachableTo: [ElementType] = [.form, .card, .container]
    let category: DocumentationCategory = .form
    let description: String = "Renders a form"
    let arguments: [Argument] = [
        Argument(name: "label", type: .string, description: "Label for the form text"),
        Argument(name: "name", type: .string, description: "Name for the form text"),
        Argument(name: "placeholder", type: .optionalString, description: "Placeholder", defaultValue: ""),
        Argument(name: "value", type: .optionalString, description: "Value if you want to pre-populate", defaultValue: ""),
    ]
    let postInitPythonFunc: String? = nil
    let exampleCode: [ExampleCode] = [
        ExampleCode(setup: nil, arguments: [ExampleArgument(argumentName: "label", argumentValue: .string("Name")), ExampleArgument(argumentName: "name", argumentValue: .string("name")), ExampleArgument(argumentName: "placeholder", argumentValue: .string("John Doe"))]),
        ExampleCode(setup: nil, arguments: [ExampleArgument(argumentName: "label", argumentValue: .string("Email")), ExampleArgument(argumentName: "name", argumentValue: .string("email")), ExampleArgument(argumentName: "placeholder", argumentValue: .string("test@test.com"))])
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let name = arguments.get("name").templateVariable(in: renderingSystem)
        let label = arguments.get("label").templateVariable(in: renderingSystem)
        let placeholder = arguments.get("placeholder").templateVariable(in: renderingSystem)        
        let value = arguments.get("value").templateVariable(in: renderingSystem)        

        return """
        <div class="mb-6">
            <label for="\(name)" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">\(label)</label>
            <input type="text" name="\(name)" value="\(value)" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="\(placeholder)" required>
        </div>
        """
    }
}

struct FormEmailElement: Element {
    let elementType: ElementType = .formemail
    let name: String = "Form Email"
    let attachableTo: [ElementType] = [.form, .card, .container]
    let category: DocumentationCategory = .form
    let description: String = "Renders a form email"
    let arguments: [Argument] = [
        Argument(name: "label", type: .optionalString, description: "Label for the form email", defaultValue: "Your E-mail"),
        Argument(name: "name", type: .optionalString, description: "Name for the form email", defaultValue: "email"),
        Argument(name: "placeholder", type: .optionalString, description: "Placeholder", defaultValue: "user@example.com")
    ]
    let postInitPythonFunc: String? = nil
    let exampleCode: [ExampleCode] = [
        ExampleCode(setup: nil, arguments: [ExampleArgument(argumentName: "label", argumentValue: .string("Email")), ExampleArgument(argumentName: "name", argumentValue: .string("email")), ExampleArgument(argumentName: "placeholder", argumentValue: .string("test@pycob.com"))])
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let name = arguments.get("name").templateVariable(in: renderingSystem)
        let label = arguments.get("label").templateVariable(in: renderingSystem)
        let placeholder = arguments.get("placeholder").templateVariable(in: renderingSystem)        

        return """
        <div class="mb-6">
            <label for="\(name)" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">\(label)</label>
            <input type="email" name="\(name)" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="\(placeholder)" required>
        </div>
        """
    }
}

struct FormPasswordElement: Element {
    let elementType: ElementType = .formpassword
    let name: String = "Form Password"
    let attachableTo: [ElementType] = [.form, .card, .container]
    let category: DocumentationCategory = .form
    let description: String = "Renders a form password"
    let arguments: [Argument] = [
        Argument(name: "label", type: .optionalString, description: "Label for the form password", defaultValue: "Password"),
        Argument(name: "name", type: .optionalString, description: "Name for the form password", defaultValue: "password"),
        Argument(name: "placeholder", type: .optionalString, description: "Placeholder", defaultValue: "password")
    ]
    let postInitPythonFunc: String? = nil
    let exampleCode: [ExampleCode] = [
        ExampleCode(setup: nil, arguments: [ExampleArgument(argumentName: "label", argumentValue: .string("Password")), ExampleArgument(argumentName: "name", argumentValue: .string("password")), ExampleArgument(argumentName: "placeholder", argumentValue: .string("********"))])
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let name = arguments.get("name").templateVariable(in: renderingSystem)
        let label = arguments.get("label").templateVariable(in: renderingSystem)
        let placeholder = arguments.get("placeholder").templateVariable(in: renderingSystem)        

        return """
        <div class="mb-6">
            <label for="\(name)" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">\(label)</label>
            <input type="password" name="\(name)" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="\(placeholder)" required>
        </div>
        """
    }
}

struct FormSelectElement: Element {
    let elementType: ElementType = .formselect
    let name: String = "Form Select"
    let attachableTo: [ElementType] = [.form, .card, .container]
    let category: DocumentationCategory = .form
    let description: String = "Renders a form select"
    let arguments: [Argument] = [
        Argument(name: "label", type: .string, description: "Label for the form select"),
        Argument(name: "name", type: .string, description: "Name for the form select"),
        Argument(name: "options", type: .untyped, description: "Options for the form select"),
        Argument(name: "value", type: .optionalString, description: "Selected value", defaultValue: ""),
    ]
    let postInitPythonFunc: String? = """
    self.components = []

    if value == "":
        self.components.append(HtmlComponent('<option value="" selected disabled hidden>Select an option</option>'))

    for option in self.options:
        if isinstance(option, str):
            if option == value:
                self.components.append(SelectoptionComponent(label=option, value=option, selected='selected'))
            else:
                self.components.append(SelectoptionComponent(label=option, value=option))
        else:
            if option['value'] == value:
                self.components.append(SelectoptionComponent(label=option['label'], value=option['value'], selected='selected'))
            else:
                self.components.append(SelectoptionComponent(label=option['label'], value=option['value']))
    """
    let exampleCode: [ExampleCode] = [
        ExampleCode(setup: nil, arguments: [ExampleArgument(argumentName: "label", argumentValue: .string("Select")), ExampleArgument(argumentName: "name", argumentValue: .string("select")), ExampleArgument(argumentName: "options", argumentValue: .raw("[{'value': 'US', 'label': 'United States'}, {'value': 'CA', 'label': 'Canada'}]"))])
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let name = arguments.get("name").templateVariable(in: renderingSystem)
        let label = arguments.get("label").templateVariable(in: renderingSystem)
        let options = arguments.get("options").templateVariable(in: renderingSystem)

        let components = Argument(name: "components", type: .elements, description: "").templateVariable(in: renderingSystem)

        return """
        <div class="mb-6">
            <label for="\(name)" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">\(label)</label>
            <select id="\(name)" name="\(name)" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                \(components)
            </select>
        </div>
        """
    }
}

struct FormHiddenElement: Element {
    let elementType: ElementType = .formhidden
    let name: String = "Form Hidden Field"
    let attachableTo: [ElementType] = [.form]
    let category: DocumentationCategory = .form
    let description: String = "Renders a hidden field on a form. This is useful for carrying state between pages without having to store data in the database."
    let arguments: [Argument] = [
        Argument(name: "name", type: .string, description: "Name for the form hidden"),
        Argument(name: "value", type: .string, description: "Value for the form hidden"),
    ]
    let postInitPythonFunc: String? = nil
    let exampleCode: [ExampleCode] = [
        ExampleCode(setup: nil, arguments: [ExampleArgument(argumentName: "name", argumentValue: .string("hidden")), ExampleArgument(argumentName: "value", argumentValue: .string("hidden"))])
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let name = arguments.get("name").templateVariable(in: renderingSystem)
        let value = arguments.get("value").templateVariable(in: renderingSystem)

        return """
        <input type="hidden" name="\(name)" value="\(value)">
        """
    }
}

struct SelectOptionElement: Element {
    let elementType: ElementType = .selectoption
    let name: String = "Select Option"
    let attachableTo: [ElementType] = [.formselect]
    let category: DocumentationCategory = .internal
    let description: String = "Renders a select option"
    let arguments: [Argument] = [
        Argument(name: "label", type: .string, description: "Label for the select option"),
        Argument(name: "value", type: .string, description: "Value for the select option"),
        Argument(name: "selected", type: .optionalString, description: "Use 'selected' if this is selected", defaultValue: ""),
    ]
    let postInitPythonFunc: String? = nil
    let exampleCode: [ExampleCode] = [
        ExampleCode(setup: nil, arguments: [ExampleArgument(argumentName: "label", argumentValue: .string("United States")), ExampleArgument(argumentName: "value", argumentValue: .string("US"))])
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let label = arguments.get("label").templateVariable(in: renderingSystem)
        let value = arguments.get("value").templateVariable(in: renderingSystem)
        let selected = arguments.get("selected").templateVariable(in: renderingSystem)

        return """
        <option value="\(value)" \(selected)>\(label)</option>
        """
    }
}

struct TextAreaElement: Element {
    let elementType: ElementType = .formtextarea
    let name: String = "Text Area"
    let attachableTo: [ElementType] = [.form, .card, .container]
    let category: DocumentationCategory = .form
    let description: String = "Renders a text area"
    let arguments: [Argument] = [
        Argument(name: "label", type: .optionalString, description: "Label for the text area", defaultValue: "Your Message"),
        Argument(name: "name", type: .optionalString, description: "Name for the text area", defaultValue: "message"),
        Argument(name: "placeholder", type: .optionalString, description: "Placeholder", defaultValue: "Leave a comment..."),
        Argument(name: "value", type: .optionalString, description: "Value if you want to pre-populate", defaultValue: ""),
    ]
    let postInitPythonFunc: String? = nil
    let exampleCode: [ExampleCode] = [
        ExampleCode(setup: nil, arguments: [ExampleArgument(argumentName: "label", argumentValue: .string("Message")), ExampleArgument(argumentName: "name", argumentValue: .string("message")), ExampleArgument(argumentName: "placeholder", argumentValue: .string("Your message"))])
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let name = arguments.get("name").templateVariable(in: renderingSystem)
        let label = arguments.get("label").templateVariable(in: renderingSystem)
        let placeholder = arguments.get("placeholder").templateVariable(in: renderingSystem)        
        let value = arguments.get("value").templateVariable(in: renderingSystem)        

        return """
        <div class="mb-6">
            <label for="\(name)" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">\(label)</label>
            <textarea name="\(name)" rows="4" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="\(placeholder)">\(value)</textarea>
        </div>
        """
    }
}

struct FormSubmitElement: Element {
    let elementType: ElementType = .formsubmit
    let name: String = "Form Submit"
    let attachableTo: [ElementType] = [.form, .card, .container]
    let category: DocumentationCategory = .form
    let description: String = "Renders a form submit button"
    let arguments: [Argument] = [Argument(name: "label", type: .optionalString, description: "Label for the form submit button", defaultValue: "Submit")]
    let postInitPythonFunc: String? = nil
    let exampleCode: [ExampleCode] = [
        ExampleCode(setup: nil, arguments: [ExampleArgument(argumentName: "label", argumentValue: .string("Submit"))]),
        ExampleCode(setup: nil, arguments: [ExampleArgument(argumentName: "label", argumentValue: .string("Save"))])
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let label = arguments.get("label")

        return """
        <button type="submit" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">\(label.templateVariable(in: renderingSystem))</button>
        """
    }
}

struct RawTableElement: Element {
    let elementType: ElementType = .rawtable
    let name: String = "Raw HTML Table"
    let attachableTo: [ElementType] = [.page, .card, .form]
    let category: DocumentationCategory = .table
    let description: String = "Renders a table manually by constructing the table header, body, content, etc.. This is useful if you want to customize the table more than what the other table functions allow. Most of the time you'll use the other table functions instead of this one."
    let arguments: [Argument] = [
        Argument(name: "components", type: .elements, description: "Components to render in the table")
    ]
    let postInitPythonFunc: String? = nil
    let exampleCode: [ExampleCode] = [
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let components = arguments.get("components").templateVariable(in: renderingSystem)

        return """
        <div class="relative overflow-x-auto shadow-md mb-5 sm:rounded-lg">
            <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
                \(components)
            </table>
        </div>
        """
    }
}

struct TableHeadElement: Element {
    let elementType: ElementType = .tablehead
    let name: String = "Table Head"
    let attachableTo: [ElementType] = [.rawtable]
    let category: DocumentationCategory = .table
    let description: String = "Renders a table head"
    let arguments: [Argument] = [
        Argument(name: "components", type: .elements, description: "Components to render in the table head")
    ]
    let postInitPythonFunc: String? = nil
    let exampleCode: [ExampleCode] = [
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let components = arguments.get("components").templateVariable(in: renderingSystem)

        return """
        <thead class="bg-gray-50 dark:bg-gray-800">
            <tr>
                \(components)
            </tr>
        </thead>
        """
    }
}

struct TableRowElement: Element {
    let elementType: ElementType = .tablerow
    let name: String = "Table Row"
    let attachableTo: [ElementType] = [.rawtable, .tablehead, .tablebody]
    let category: DocumentationCategory = .table
    let description: String = "Renders a table row"
    let arguments: [Argument] = [
        Argument(name: "components", type: .elements, description: "Components to render in the table row")
    ]
    let postInitPythonFunc: String? = nil
    let exampleCode: [ExampleCode] = [
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let components = arguments.get("components").templateVariable(in: renderingSystem)

        return """
        <tr class="border-t border-gray-200 dark:border-gray-700">
            \(components)
        </tr>
        """
    }
}

struct TableColElement: Element {
    let elementType: ElementType = .tablecol
    let name: String = "Table Column"
    let attachableTo: [ElementType] = [.tablehead, .tablerow]
    let category: DocumentationCategory = .table
    let description: String = "Renders a table column"
    let arguments: [Argument] = [
        Argument(name: "components", type: .elements, description: "Components to render in the table column")
    ]
    let postInitPythonFunc: String? = nil
    let exampleCode: [ExampleCode] = [
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let components = arguments.get("components").templateVariable(in: renderingSystem)

        return """
        <td class="px-6 py-4 whitespace-nowrap">
            \(components)
        </td>
        """
    }
}

struct TableCellElement: Element {
    let elementType: ElementType = .tablecell
    let name: String = "Table Cell"
    let attachableTo: [ElementType] = [.tablehead, .tablerow]
    let category: DocumentationCategory = .table
    let description: String = "Renders a table cell"
    let arguments: [Argument] = [
        Argument(name: "value", type: .string, description: "String to render in the table cell")
    ]
    let postInitPythonFunc: String? = nil
    let exampleCode: [ExampleCode] = [
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let value = arguments.get("value").templateVariable(in: renderingSystem)

        return """
        <td class="px-6 py-4 whitespace-nowrap">
            \(value)
        </td>
        """
    }
}

struct TableCellHeaderElement: Element {
    let elementType: ElementType = .tablecellheader
    let name: String = "Table Cell Header"
    let attachableTo: [ElementType] = [.tablehead, .tablerow]
    let category: DocumentationCategory = .table
    let description: String = "Renders a table cell header"
    let arguments: [Argument] = [
        Argument(name: "value", type: .string, description: "String to render in the table cell header")
    ]
    let postInitPythonFunc: String? = nil
    let exampleCode: [ExampleCode] = [
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let value = arguments.get("value").templateVariable(in: renderingSystem)

        return """
        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
            \(value)
        </th>
        """
    }
}

struct TableBodyElement: Element {
    let elementType: ElementType = .tablebody
    let name: String = "Table Body"
    let attachableTo: [ElementType] = [.rawtable]
    let category: DocumentationCategory = .table
    let description: String = "Renders a table body"
    let arguments: [Argument] = [
        Argument(name: "components", type: .elements, description: "Components to render in the table body")
    ]
    let postInitPythonFunc: String? = nil
    let exampleCode: [ExampleCode] = [
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let components = arguments.get("components").templateVariable(in: renderingSystem)

        return """
        <tbody>
            \(components)
        </tbody>
        """
    }
}

struct PandasTableElement: Element {
    let elementType: ElementType = .pandastable
    let name: String = "Pandas Table"
    let attachableTo: [ElementType] = [.page, .card, .container]
    let category: DocumentationCategory = .advanced
    let description: String = "Renders a pandas table"
    let arguments: [Argument] = [
        Argument(name: "dataframe", type: .untyped, description: "Dataframe to render"),
        Argument(name: "hide_fields", type: .list, description: "List of fields to hide"),
        Argument(name: "action_buttons", type: .elements, description: "Row actions to render")
    ]
    let postInitPythonFunc: String? = nil
    let exampleCode: [ExampleCode] = [
        ExampleCode(setup: ["""
        data = {
        "calories": [420, 380, 390],
        "duration": [50, 40, 45],
        "large_numbers": [9000, 9000000, 9000000000],
        }
        """
        , "df = pd.DataFrame(data)"
        ], arguments: [ExampleArgument(argumentName: "dataframe", argumentValue: .raw("df"))])
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        return "TODO: Advanced Component"
    }
}

struct PlotlyFigureElement: Element {
    let elementType: ElementType = .plotlyfigure
    let name: String = "Plotly Figure"
    let attachableTo: [ElementType] = [.page, .card, .container]
    let category: DocumentationCategory = .charts
    let description: String = "Renders a plotly figure"
    let arguments: [Argument] = [
        Argument(name: "fig", type: .untyped, description: "Figure to render"),
        Argument(name: "id", type: .optionalString, description: "Unique ID for this element. Will default to a UUID.", defaultValue: "")
    ]

    let postInitPythonFunc: String? = """
    if id == "":
        self.id = str(uuid.uuid4())
    self.fig = fig.to_json()
    """
    let exampleCode: [ExampleCode] = [
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let fig = arguments.get("fig").templateVariable(in: renderingSystem)
        let id = arguments.get("id").templateVariable(in: renderingSystem)

        return """
        <div id="\(id)"></div>
        <script>
            config = \(fig)
            Plotly.newPlot( document.getElementById("\(id)"), config, {responsive: true} );
        </script>
        """
    }
}

struct DataGridElement: Element {
    let elementType: ElementType = .datagrid
    let name: String = "Data Grid"
    let attachableTo: [ElementType] = [.page, .card]
    let category: DocumentationCategory = .advanced
    let description: String = "Renders a data grid"
    let arguments: [Argument] = [
        Argument(name: "dataframe", type: .untyped, description: "Dataframe to render"),
        Argument(name: "action_buttons", type: .elements, description: "Row actions to render")
    ]

    let postInitPythonFunc: String? = nil
    let exampleCode: [ExampleCode] = [
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        return "TODO: Advanced Component"
    }
}

struct RowActionElement: Element {
    let elementType: ElementType = .rowaction
    let name: String = "Row Action"
    let attachableTo: [ElementType] = []
    let category: DocumentationCategory = .internal
    let description: String = "Renders a row action"
    let arguments: [Argument] = [
        Argument(name: "label", type: .string, description: "Label for the button. Use {col_name} to use a column value. If you use just the column value, the button will replace that column. If you use a static string, a column will be added for the button."),
        Argument(name: "url", type: .string, description: "URL to navigate to when the button is clicked. Use {col_name} to include the column value in the link"),
        Argument(name: "classes", type: .optionalString, description: "Classes to add to the button", defaultValue: ""),
        Argument(name: "open_in_new_window", type: .optionalBool, description: "Open the link in a new window", defaultValue: "True"),
    ]
    let postInitPythonFunc: String? = nil
    let exampleCode: [ExampleCode] = [
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        return "TODO: Internal Component"
    }
}

struct ScriptStatusElement: Element {
    let elementType: ElementType = .scriptstatus
    let name: String = "Script Status"
    let attachableTo: [ElementType] = [.page, .card, .container]
    let category: DocumentationCategory = .internal
    let description: String = "Shows the status of a script execution and redirects to a new page when complete"
    let arguments: [Argument] = [
        Argument(name: "job_id", type: .string, description: "Job id to check the status of"),
        Argument(name: "redirect_url", type: .string, description: "URL to redirect to when the script is complete"),
    ]
    let postInitPythonFunc: String? = nil
    let exampleCode: [ExampleCode] = [
    ]

    func toTailwindHtmlTemplate(in renderingSystem: RenderingSystem) -> String {
        let jobId = arguments.get("job_id").templateVariable(in: renderingSystem)
        let redirectUrl = arguments.get("redirect_url").templateVariable(in: renderingSystem)

    return """
    <script type="module">
        import { initializeApp } from 'https://www.gstatic.com/firebasejs/9.17.1/firebase-app.js'
            
        import { getFirestore, doc, onSnapshot } from 'https://www.gstatic.com/firebasejs/9.17.1/firebase-firestore.js'

        // TODO: Replace the following with your app's Firebase project configuration
        const firebaseConfig = {
            projectId: "pycob-prod"
        };

        // Initialize Firebase
        const app = initializeApp(firebaseConfig);

        let db = getFirestore();

        const unsub = onSnapshot(doc(db, "users", "test", "_jobs", "\(jobId)"), (doc) => {
            console.log("Current data: ", doc.data());
            document.getElementById("\(jobId)").innerHTML = doc.data().status;

            if (doc.data().status == "complete") {
                unsub();
                window.location.href = "\(redirectUrl)";
            }
        });
    </script>
    <div class="flex items-center justify-center p-5 border border-gray-200 rounded-lg bg-gray-50 dark:bg-gray-800 dark:border-gray-700">
        <svg aria-hidden="true" class="w-8 h-8 mr-2 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/><path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill"/></svg>
        <div id="\(jobId)" class="px-3 py-1 text-xs font-medium leading-none text-center text-blue-800 bg-blue-200 rounded-full animate-pulse dark:bg-blue-900 dark:text-blue-200">waiting...</div>
    </div>
    """
    }
}

struct PyPup: Codable {
    let name: String
    let title: String
    let contents: [[String: ArgumentInstance]]
}

enum ArgumentInstance: Codable {
    case string(String)
    case int(Int)
    case bool(Bool)
    case raw(String)

    init(from decoder: Decoder) throws {
        let container = try decoder.singleValueContainer()
        if let x = try? container.decode(String.self) {
            self = .string(x)
            return
        }
        if let x = try? container.decode(Int.self) {
            self = .int(x)
            return
        }
        if let x = try? container.decode(Bool.self) {
            self = .bool(x)
            return
        }
        throw DecodingError.typeMismatch(ArgumentInstance.self, DecodingError.Context(codingPath: decoder.codingPath, debugDescription: "Wrong type for ArgumentInstance"))
    }

    func encode(to encoder: Encoder) throws {
        var container = encoder.singleValueContainer()
        switch self {
        case .raw(let x):
            try container.encode(x)
        case .string(let x):
            try container.encode(x)
        case .int(let x):
            try container.encode(x)
        case .bool(let x):
            try container.encode(x)
        }
    }

    func toString() -> String {
        switch self {
        case .string(let x):
            return x
        case .int(let x):
            return String(x)
        case .bool(let x):
            switch x {
            case true:
                return "True"
            case false:
                return "False"
            }
        case .raw(let variable):
            return variable
        }
    }

    func withQuotes() -> String {
        switch self {
        case .string(let x):
            return "'\(x)'"
        case .int(let x):
            return String(x)
        case .bool(let x):
            switch x {
            case true:
                return "True"
            case false:
                return "False"
            }
        case .raw(let x):
            return x
        }
    }
}

// typealias PyPupContent = [String: ArgumentInstance] 

extension Encodable {
  func asDictionary() throws -> [String: Any] {
    let data = try JSONEncoder().encode(self)
    guard let dictionary = try JSONSerialization.jsonObject(with: data, options: .allowFragments) as? [String: Any] else {
      throw NSError()
    }
    return dictionary
  }
}

print("Generating...")

var outputJson: String = ""

func toJson(_ anything: Encodable) -> String {
    let encoder = JSONEncoder()
    encoder.outputFormatting = .prettyPrinted
    let jsonData = try! encoder.encode(anything)
    let jsonString = String(data: jsonData, encoding: .utf8)!
    return jsonString
}

func pyPupFromJsonFile(_ path: String) -> PyPup {
    let jsonData = try! Data(contentsOf: URL(fileURLWithPath: path))
    let decoder = JSONDecoder()
    let pp = try! decoder.decode(PyPup.self, from: jsonData)
    return pp
}

outputJson = "[" + ElementType.allCases.map { toJson($0.element) } .joined(separator: ",\n") + "]"

try outputJson.write(toFile: "spec/spec.json", atomically: true, encoding: .utf8)

let generatedComponents: String = Generator.generatePyVibe()

let advancedPy: String = try! String(contentsOfFile: "generator/includes/advanced.py.txt")

let allComponents: String = generatedComponents + "\n#\n#\n# Begin Manual Code\n#\n#\n#\n" + advancedPy

try allComponents.write(toFile: "src/pyvibe/__init__.py", atomically: true, encoding: .utf8)

print("Done")