from config0_publisher.terraform import TFConstructor


def run(stackargs):
    import random

    # instantiate authoring stack
    stack = newStack(stackargs)

    stack.parse.add_required(key=<required_variable>)
    stack.parse.add_optional(key=<optional_variable>)

    stack.add_execgroup("config0-publish:::contribution-starter-repo::ec2_server",  # This must correpond to the correct owner and repository
                        "tf_execgroup")  # the alias can be anything, but we use tf_execgroup to simplify things

    # Add substack
    stack.add_substack('config0-publish:::tf_executor')

    # initialize
    stack.init_variables()
    stack.init_execgroups()
    stack.init_substacks()

    # use the terraform constructor (helper)
    # but this is optional
    tf = TFConstructor(stack=stack,
                       execgroup_name=stack.tf_execgroup.name,
                       provider=<provider>,
                       resource_name=<resource_name>,
                       resource_type=<resource_type>,
                       terraform_type=<terraform_type>

    # terraform resource keys
    # to transfer to db for querying
    tf.include(keys=["id",
                      ...
                      ])

    # terraform resource keys
    # to map for ease of query in db
    tf.include(maps={"_id": "id",
                     ...})

    # resource output to show
    # on saas ui
    tf.output(keys=["id",
                    ...
                    ])

    # finalize the tf_executor
    stack.tf_executor.insert(display=True,
                             **tf.get())

    return stack.get_results()
